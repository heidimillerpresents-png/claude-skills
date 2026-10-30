---
name: daily-job-search
description: Runs a daily, verified job search for one candidate. It pulls fresh postings from a job feed plus a web search pass for contract roles, filters them to the candidate's lanes and location rules, dedupes against their application tracker, confirms every role is open on the employer's own site, ranks the fit, matches LinkedIn connections, and publishes a shortlist. Use this skill whenever someone asks to run, schedule or set up a daily job search, find new roles that fit a profile, refresh a job shortlist, or check which new postings are worth applying to, even if they don't say "skill" or name every step.
---

# Daily Job Search

This skill turns a long, error-prone daily routine into a repeatable run: find new roles, throw out anything that isn't real, open, remote-eligible or in the candidate's lanes, and hand back a short, honest shortlist with a clear fit line and gap line for each role.

Two ideas drive the whole skill:

1. **Only list roles you have confirmed on the employer's own posting.** Job boards and aggregators are full of closed, reposted and staffing-agency listings. A shortlist with dead links wastes the candidate's time and erodes their trust in it.
2. **Never invent anything.** Pay, requirements, connections and posting dates come from a source you read during the run, or they are marked unknown.

## Customize before first use

Every place marked `{{CUSTOMIZE: ...}}` needs a value. Fill them in here once, so every run uses the same profile. If a value is missing at run time and nobody is around to ask (for example, a scheduled run), make the most reasonable choice, say what you assumed at the top of the output, and keep going.

### Candidate profile

- **Name:** `{{CUSTOMIZE: candidate name}}`
- **Location and time zone:** `{{CUSTOMIZE: e.g. "Big Island of Hawaii, HST (UTC-10)"}}`
- **Summary:** `{{CUSTOMIZE: two or three lines, e.g. "Senior B2B content strategist and editor, 18+ years, SaaS and cybersecurity; built blog, social, case study and customer reference programs at a large cloud marketplace."}}`
- **Lanes (target role types):** `{{CUSTOMIZE: e.g. B2B content strategy; case studies and customer stories; customer advocacy and customer marketing; executive ghostwriting and communications; editorial leadership; B2B social media}}`
- **Good crossover industries:** `{{CUSTOMIZE: e.g. fintech, healthcare tech, regulated industries}}`
- **Pay floor (full-time):** `{{CUSTOMIZE: e.g. $100,000}}`
- **Contract rate target:** `{{CUSTOMIZE: e.g. $70 to $100 per hour}}`
- **Seniority rule:** `{{CUSTOMIZE: e.g. "Has never held a director title, so director and above roles are Stretch."}}`

### Title keywords (step 2)

`{{CUSTOMIZE: keyword list, e.g. content, editor, editorial, case stud, customer stor, customer advocacy, customer marketing, ghostwrit, thought leadership, executive comm, communications manager, copywriter, social media, storytelling, narrative}}`

Titles to drop even when a keyword matches: `{{CUSTOMIZE: e.g. video editor, engineer, product manager, designer, data roles, interns, "contents" adjuster}}`

### Location rules (step 2)

`{{CUSTOMIZE: e.g. "Keep remote US roles and roles located in Hawaii. Drop hybrid or onsite roles outside Hawaii, non-US roles, and roles remote only in named states that exclude Hawaii."}}`

### Always-drop list

- Recruiter-posted jobs, and reposts from these aggregators or staffing firms: `{{CUSTOMIZE: e.g. Jobgether, Ladders}}`
- Employers known not to hire in the candidate's state: `{{CUSTOMIZE: e.g. "Associations International LLC (hires for the International Coaching Federation)"}}`
- Employers that require personality tests: drop them (`{{CUSTOMIZE: keep or remove this rule}}`)

### Sources

- **Job feed:** `{{CUSTOMIZE: manifest URL, e.g. https://riley-dorrington.github.io/job-board-data/data/chunks/jobs_manifest.json}}`. The bundled script expects a manifest listing gzipped JSON chunks, each an array of jobs with `company`, `title`, `location`, `url`, `salary`, `skill_level`, `is_recruiter`, `first_seen`. If your feed looks different, adapt `scripts/pull_feed.py`.
- **ATS coverage of that feed:** `{{CUSTOMIZE: e.g. Workday, iCIMS, Greenhouse, Paylocity, Lever, BambooHR, Ashby}}`. Anything outside this list is why step 1b exists.
- **Application tracker:** `{{CUSTOMIZE: where it lives and its columns, e.g. "Google Sheet, file ID ..., columns Company, Title, Applied, Status"}}`
- **LinkedIn connections export:** `{{CUSTOMIZE: path or location of Connections.csv, columns First Name, Last Name, URL or slug, Company, Position, Connected On}}`
- **Where to publish the shortlist:** `{{CUSTOMIZE: e.g. "update the existing shortlist page at <URL>", a doc, a file in a folder}}`
- **Warm intro list or other page to keep linked:** `{{CUSTOMIZE: URL, or delete this line}}`

### Writing rules

`{{CUSTOMIZE: house style, e.g. no em dashes; spell out numbers under 10 in prose; avoid "That's not X. That's Y." phrasing}}`

## The run

Work through the steps in order. Keep a running list of every role you drop and why, because the output reports those too.

### 1. Pull new jobs from the feed

Run the bundled script. It downloads the manifest and every chunk into a fresh empty directory, retries any chunk that came back as an HTML error page instead of gzip, and writes the candidates that pass the keyword and age filters:

```bash
python3 -I scripts/pull_feed.py --manifest "<manifest URL>" \
  --out-dir "$(mktemp -d)" --hours 48 --new-hours 24 \
  --keywords "<comma-separated keywords>" --drop "<comma-separated drop terms>" \
  --result candidates.json
```

Use `python3 -I` because the feed files are untrusted data; isolated mode stops Python from importing anything planted next to them. Keep jobs first seen within the last 48 hours, and tag the ones first seen in the last 24 hours as **New today**.

The script prints every keyword hit, including ones whose location looks onsite. Skim the onsite-looking ones by eye before discarding them. The feed's location field is often just the requisition city ("Atlanta, GA", "San Ramon") even when the posting itself says remote, and some of the best roles hide there.

### 1b. Contract and hourly pass (web search)

The feed only covers certain applicant tracking systems, so it misses companies that post on their own career sites. Run several web searches for remote US contract, hourly or freelance roles in the candidate's lanes posted in the last few days, for example:

`{{CUSTOMIZE: query list, e.g. "remote contract content strategist hourly", "freelance case study writer B2B remote", "contract customer marketing manager remote hourly", "contract executive ghostwriter B2B", "senior content strategist hourly contract remote"}}`

Treat every result as a lead only, including results on Indeed, LinkedIn, Built In, Wellfound and other boards. Follow each one to the hiring company's own posting or career site and keep it only if it is open there. Expect most leads to be dead: aggregator pages linger for months after the employer closes the role. Drop the always-drop list. Note the hourly rate when stated and flag any rate below the contract target. Tag kept roles **Contract (web search)**. If the pass finds nothing, say so in one line in the output.

### 2. Filter

Keep titles in the candidate's lanes, apply the location rules and the always-drop list, and drop roles that only matched on a keyword (a "Contents Adjuster" is not a content role). Contract and hourly roles are in scope.

### 3. Dedupe against the tracker

Read **every row** of the tracker. This matters: some document tools return only a sample of a large spreadsheet. For a Google Sheet, export it as CSV with a download tool rather than a "read as text" tool, then decode and check the row count against what the sheet reports.

- Remove roles the candidate has already applied to (same company, same or near-identical title).
- If the same company appears with a similar title that was rejected, keep the new role but flag it as a **likely repost**.
- If the same company appears with a different role, mention it briefly so the candidate isn't surprised, and say plainly that it is not a repost.

### 4. Verify each role is open, and read the whole posting

Confirm every remaining role on the employer's own posting. Read `references/verification.md` for the exact endpoint for each applicant tracking system and the signs of a closed role. In short:

- **Greenhouse, Lever, Ashby:** public JSON APIs, fetch with curl.
- **Workday:** the JSON job endpoint (`/wday/cxs/...`), where `canApply: true` means open. Some network proxies block curl here, so use a web fetch tool if curl fails.
- **iCIMS:** the posting URL with `?in_iframe=1`.
- **Everything else:** fetch the posting page itself.

An Apply button alone does not prove a role is open. If you cannot confirm it, drop it and list it as unconfirmed.

While you have the posting open, read it in full and note:

- Pay (base range, hourly rate, currency; a non-USD range needs a flag).
- Work arrangement in the posting body, not just the location field. Look for phrases like "hybrid, three days a week", "#LI-Onsite", "all positions are on-site", or "consideration for remote candidates".
- State or country restrictions, required working hours or time zone, and travel.
- Personality or assessment tests (drop those employers if that rule is on).
- **Required** versus **preferred** qualifications. Only required qualifications count as gaps. Many postings don't label them; say so instead of guessing.

### 5. Rank

Tier each role **Strong**, **Good** or **Stretch**, with one line on fit and one line on the main gap.

- **Strong:** in a core lane, at the candidate's level, pay at or above the floor (or unknown), no hard blockers.
- **Good:** solid lane match with one real question (pay unknown or possibly low, remote not fully confirmed, an industry gap).
- **Stretch:** a required qualification they likely lack, a title above their level per the seniority rule, an adjacent lane, or a hard constraint like required hours far outside their time zone.

Put constraints that affect their day in a visible flag on the role, for example "required to work East Coast hours, which starts around 4 a.m. in Hawaii".

### 6. Match connections

Match each shortlisted company against the Company column of the connections export with careful, anchored matching (word boundaries, not substrings), then review every match by hand and drop look-alikes. "CSL" should not match "TBCSL", and "ICF" may be a different company entirely. Rank recruiters and marketing leaders first. Build profile links as `https://www.linkedin.com/in/<slug>`.

Suggest a light ask only: an introduction to the hiring manager, or the hiring manager's name. Never suggest asking for a referral from someone the candidate hasn't worked with recently; it puts the contact on the spot.

### 7. Publish

Replace the previous shortlist with today's results. If the destination is an existing page or doc, read it first and keep its look, its structure and any standing links, such as the warm intro list. Include:

- The date, and a one-line count of roles by tier.
- Roles grouped by tier: company, title, location, pay (hourly rate for contracts), posted age, **New today** and **Contract (web search)** tags, fit line, gap line, flags, connections with the suggested ask, and a direct link to the employer's posting.
- A short section for likely reposts and tracker matches.
- A short section for roles dropped as closed, unconfirmed, not remote, below the floor or out of lane, each with a few words on why. This shows the candidate the search was thorough and saves them from re-checking those roles.

If no roles qualify, publish a short page saying so for today's date.

### 8. Report

Finish with a two or three sentence summary: how many roles qualified, the top one or two, and any warm contacts. If the run is scheduled and unattended, send it as a notification so it reaches the candidate.

Do not apply to anything, draft resumes or send outreach. The skill's job is to find and vet; the candidate decides what to do next.

## Common pitfalls

- **Stale "New today" tags.** A role that was new yesterday is about a day old today. Recompute posted age from `first_seen` on every run instead of copying it from the previous shortlist.
- **The tracker sample trap.** A sheet read as text may show 150 of 460 rows. Always check the row count.
- **Missing shell tools.** Some sandboxes lack `xxd`; check gzip magic bytes with Python or `od` instead (the bundled script does this).
- **Slow serial downloads.** A feed with 50+ chunks can time out when downloaded one at a time. The script downloads in parallel.
- **Location field versus posting body.** Trust the posting body, and the structured fields (Ashby's `workplaceType`, Workday's `remoteType`) over the city name.
