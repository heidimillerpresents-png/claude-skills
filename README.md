# Claude Skills

Custom skills for use with Claude (Anthropic's AI).

## job-listing-strategic-analysis

Runs a management-consulting-style analysis of a company's job listings
to identify the real business pain points behind an open role, for use
when applying to that role. See `job-listing-strategic-analysis/SKILL.md`

## resume-tailoring-pipeline

Triages a batch of job postings for fit, then produces a tailored
two-page resume for the ones worth pursuing. See
`resume-tailoring-pipeline/SKILL.md`.

**Note:** this skill's formatting rules (comp floor, contact-line order,
resume length, style preferences) reflect my own defaults. If you use
it, edit the rules in the SKILL.md to match your own resume standards
before running it.

## case-study-interview-to-draft-pipeline

A structured, repeatable process for turning a customer nomination into
a finished case study, from intake through interviews to a polished
draft, with AI-assisted drafting at each stage. Originally used CoPilot; now skilled for Claude. See
`case-study-interview-to-draft-pipeline/SKILL.md`.

## decision-maker-outreach-drafter

Researches a named hiring manager or decision-maker, then drafts a
short, specific first-touch or follow-up outreach message grounded in
that research. Pairs well with `job-listing-strategic-analysis` when
both are run for the same company. See
`decision-maker-outreach-drafter/SKILL.md`.

## linkedin-profile-review

A Claude Skill that reviews a LinkedIn profile and returns prioritized, actionable feedback for a job search: experience-section date errors, photo/cover photo, headline, bullet quality, and connection count.

### Important: no live LinkedIn access

Claude cannot browse to LinkedIn URLs — this skill works from pasted profile content and/or an uploaded photo, not from a URL. Paste in the headline, About section, experience history, and connection count, and attach a screenshot if you want the photo reviewed.

### Install

Claude Code / CLI agents — clone and drop into your skills directory:
git clone https://github.com/<your-username>/linkedin-profile-review.git
cp -r linkedin-profile-review ~/.claude/skills/

or, project-local:
cp -r linkedin-profile-review .claude/skills/


Claude.ai / API — upload SKILL.md (or the packaged .skill file) directly wherever your Claude client supports skill uploads.

### Use

Paste a profile's content (and a photo, if you want it critiqued) and ask for a review, feedback, or an audit. The skill triggers automatically on that pattern — no special phrasing needed.

### License

MIT — use, copy, adapt.
