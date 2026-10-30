#!/usr/bin/env python3
"""Download a chunked job feed and write the recent, keyword-matching jobs.

Run with `python3 -I` so nothing in the download directory can be imported.

Expected feed shape (adapt the loading code in main() if yours differs):
  manifest JSON: {"chunks": ["jobs_chunk_0.json.gz", ...], ...}
  each chunk:    gzipped JSON array of jobs with company, title, location,
                 url, salary, skill_level, is_recruiter, first_seen (ISO 8601)
Chunks are fetched from the manifest's directory unless --base-url is given.
"""
import argparse
import concurrent.futures as cf
import gzip
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

GZIP_MAGIC = b"\x1f\x8b"


def fetch(url, dest, tries=3):
    """Download with curl (respects proxy settings); retry non-gzip responses."""
    for attempt in range(tries):
        subprocess.run(["curl", "-sS", "--max-time", "90", "-o", dest, url], check=False)
        try:
            with open(dest, "rb") as f:
                if f.read(2) == GZIP_MAGIC:
                    return True
        except FileNotFoundError:
            pass
        time.sleep(2 * (attempt + 1))
    return False


def parse_time(value):
    try:
        t = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return t if t.tzinfo else t.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True, help="URL of jobs_manifest.json")
    ap.add_argument("--base-url", help="chunk directory URL (default: manifest's directory)")
    ap.add_argument("--out-dir", required=True, help="fresh empty directory for downloads")
    ap.add_argument("--hours", type=float, default=48, help="keep jobs first seen within N hours")
    ap.add_argument("--new-hours", type=float, default=24, help="tag jobs newer than N hours as new")
    ap.add_argument("--keywords", required=True, help="comma-separated title keywords")
    ap.add_argument("--drop", default="", help="comma-separated title terms to drop")
    ap.add_argument("--drop-companies", default="jobgether,ladders", help="comma-separated")
    ap.add_argument("--result", default="candidates.json")
    ap.add_argument("--workers", type=int, default=10)
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    base = args.base_url or args.manifest.rsplit("/", 1)[0]
    man_path = os.path.join(args.out_dir, "jobs_manifest.json")
    subprocess.run(["curl", "-sS", "-o", man_path, args.manifest], check=True)
    with open(man_path) as f:
        manifest = json.load(f)
    chunks = manifest["chunks"]
    print("manifest:", {k: v for k, v in manifest.items() if k != "chunks"}, f"{len(chunks)} chunks")

    with cf.ThreadPoolExecutor(args.workers) as pool:
        results = dict(zip(chunks, pool.map(
            lambda c: fetch(f"{base}/{c}", os.path.join(args.out_dir, c)), chunks)))
    bad = [c for c, ok in results.items() if not ok]
    if bad:
        print("WARNING: chunks still not gzip after retries:", bad, file=sys.stderr)

    jobs = []
    for c in chunks:
        if results[c]:
            with gzip.open(os.path.join(args.out_dir, c)) as f:
                jobs.extend(json.load(f))
    now = datetime.now(timezone.utc)
    kw = re.compile("|".join(re.escape(k.strip()) for k in args.keywords.split(",") if k.strip()), re.I)
    drop_terms = [d.strip() for d in args.drop.split(",") if d.strip()]
    drop = re.compile("|".join(re.escape(d) for d in drop_terms), re.I) if drop_terms else None
    drop_cos = [d.strip().lower() for d in args.drop_companies.split(",") if d.strip()]

    out = []
    for j in jobs:
        seen = parse_time(j.get("first_seen"))
        if not seen or now - seen > timedelta(hours=args.hours):
            continue
        title = j.get("title") or ""
        if not kw.search(title) or (drop and drop.search(title)):
            continue
        if j.get("is_recruiter") or any(d in (j.get("company") or "").lower() for d in drop_cos):
            continue
        age = (now - seen).total_seconds() / 3600
        j["age_hours"] = round(age, 1)
        j["new_today"] = age <= args.new_hours
        out.append(j)

    out.sort(key=lambda j: (j["company"] or "").lower())
    with open(args.result, "w") as f:
        json.dump(out, f, indent=1)
    print(f"{len(jobs)} jobs in feed; {len(out)} recent keyword matches -> {args.result}")
    for j in out:
        sal = (j.get("salary") or {}).get("median") if isinstance(j.get("salary"), dict) else j.get("salary")
        print(f"{j['age_hours']:>5}h | {'NEW' if j['new_today'] else '   '} | {j['company']} | "
              f"{j['title']} | {j.get('location')} | est {sal} | {j['url']}")


if __name__ == "__main__":
    main()
