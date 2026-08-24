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
