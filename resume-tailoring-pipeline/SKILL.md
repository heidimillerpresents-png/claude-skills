---
name: resume-tailoring-pipeline
description: Triages one or more job postings for fit, then produces a tailored two-page resume following the candidate's established formatting rules (no em dashes, no comma splices, honest gap-flagging instead of overclaiming). Use this whenever the user has a batch of job postings they're considering and wants them screened for fit before deciding which to pursue, or has a single posting they want turned into a tailored resume. Not for cover letter drafting alone, and not for interview prep.
---

# Resume Tailoring Pipeline

## Purpose

Job searching at volume creates two failure modes: applying to roles that are a poor fit (wasted effort, no callback), and applying to good-fit roles with a generic resume (also no callback). This skill front-loads a fast fit check across a batch of postings, then only invests full tailoring effort in the postings worth pursuing.

## Stage 0: Triage (when multiple postings are provided)

If the user gives you two or more job postings at once, don't jump straight to tailoring. Run this pass first:

1. For each posting, do a fast fit read: does the required experience, seniority level, domain, comp (if listed), and location/remote policy roughly match the candidate's floor and background?
2. Flag genuine gaps and mismatches directly and specifically — not "some experience may be needed" but the actual missing credential, skill, or years-of-experience shortfall.
3. Note where the user has told you they've already run the posting through LinkedIn's free AI job-match check. Treat any verdict other than a clean "matches the qualifications well" as a signal there's a real gap worth investigating before spending time tailoring — ask what the AI flagged, if the user hasn't already said, and factor that into your own fit read rather than re-deriving fit from scratch.
4. Rank or group the postings: strong fit / stretch worth pursuing / skip, with a one-line reason for each.
5. Confirm with the user which postings to move into Stage 1 rather than assuming — a "stretch" role may still be worth pursuing for reasons beyond pure fit (comp, company, timing).

Skip this stage entirely if the user provides a single posting and clearly wants it tailored, not screened.

## Stage 1: Tailoring

For each posting the user wants to move forward on:

1. **Strategic read first, if not already done.** Understand what the posting is really asking for before touching the resume — what's the actual seniority bar, what's the real scope, what would make a hiring manager say yes.
2. **Match real experience to real requirements.** Pull from the candidate's full work history to find the closest honest match for each requirement. Do not invent titles, dates, or scope that didn't happen.
3. **Flag gaps rather than papering over them.** If a requirement has no honest match, say so plainly rather than stretching a tangential credential to cover it; the user decides how (or whether) to address the gap in a cover letter.
4. **Apply house formatting rules, without exception:**
   - Two-page maximum
   - No em dashes, anywhere
   - No comma splices; where two complete sentences are being joined, use a semicolon, not a comma
   - No meta-commentary phrases on resume bullets (e.g. "not a bridge," "relates directly to this job") — state the credential itself, let it speak for its relevance
   - Contact line order: LinkedIn, then writing/content portfolio, then GitHub
   - Remote-only, six-figure minimum, FTE preferred with contract treated as a bridge, unless the user says otherwise for a specific posting
   - Single-column, no tables or tab-stops, MM/YYYY dates — this format survives ATS parsing (particularly Workday) far more reliably than a visually richer layout
5. **Never use "most recently" or similar current-framing language** for a role that has already ended — check dates before applying that kind of phrasing.

## Output

- A tailored resume following the rules above, in the candidate's standard build format.
- A short, direct summary of what was changed or emphasized for this specific posting and why.
- Any gaps that were flagged but not resolved, stated plainly so the user can decide whether to address them elsewhere (cover letter, interview).
