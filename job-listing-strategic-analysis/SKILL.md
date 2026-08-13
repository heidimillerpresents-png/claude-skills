---
name: job-listing-strategic-analysis
description: Runs a McKinsey/BCG/Bain-style strategic analysis of a company's job listings to uncover the real, unstated business pain points behind an open role, using consulting frameworks and web research on the company and its competitors. Produces a strategic brief a job candidate can use to position themselves as solving problems beyond the job description, rather than just matching keywords to a resume. Use this whenever the user pastes or references job listings and wants to understand a hiring manager's real motivations, competitive pressures, or organizational pain points for a specific role they're applying to — not for generic resume tailoring or cover letter writing alone.
---

# Job Listing Strategic Analysis

## Purpose

A job listing is written to attract candidates without tipping off competitors. Underneath the soft language ("fast-paced environment," "cross-functional collaboration") are usually specific, inferable business problems. This skill reads listings the way a management consultant would read a client's RFP: as evidence of an underlying strategic situation, not just a set of requirements.

The output should let the candidate walk into an application (or interview) with a point of view on the business, not just a list of matched qualifications.

## Inputs needed

Before running the analysis, confirm you have:

1. **The job listing(s)** — ideally several open roles at the company at once (a "snapshot" of the hiring portal), since patterns across postings are more informative than a single listing.
2. **The specific role the candidate is applying to.**
3. **The candidate's relevant background**, so the final output can connect their qualifications to the pain points identified (skip this if the user only wants the company-side analysis).

If any of this is missing, ask before proceeding — don't guess at the company or role.

## Process

1. **Read across all listings, not just the target role.** Look for repeated language, repeated required skills, seniority patterns, and roles that seem to cluster around the same initiative. A pattern across 3+ listings is a stronger signal than a phrase in one.

2. **Identify what's being under-stated.** Soft phrases usually map to concrete pain points:
   - "Fast-paced, ambiguous environment" → understaffed, or scaling faster than process can support
   - "Cross-functional stakeholder management" → org has friction or competing priorities between teams
   - Multiple similar roles posted at once → a function is being built out or backfilled after attrition
   - A skill appearing suddenly across postings that wasn't there before → a new strategic priority or a recent gap (departure, failed initiative, new competitive threat)

3. **Map upstream and downstream effects.** What has to be true upstream (org structure, recent events, market pressure) for this role to exist right now? What breaks downstream if this role is unfilled or fails?

4. **Consider the hiring manager's likely position.** They have a budget, a boss they answer to, and a problem they're accountable for solving. What does their success look like in 6 months? What are they personally exposed on?

5. **Research beyond the listings.** Use web search to check:
   - The company's own blog, press releases, and investor materials (if public) for stated priorities
   - Recent news (layoffs, funding, leadership changes, product launches)
   - Competitors' job listings for the same function, to see if this is an industry-wide move or company-specific
   - Industry/analyst commentary on the company's competitive position

6. **Apply frameworks only where they add real insight** — don't force all of them in. Reach for:
   - **SWOT** for a quick internal/external snapshot
   - **PESTLE** if macro or regulatory factors plausibly explain the timing
   - **Porter's Five Forces** if competitive dynamics explain the pain point
   - **BCG Growth-Share Matrix** if the role sits within a specific product/business line
   - Trust Insights' **5P Framework** (People, Process, Platform, Performance, Purpose) works well specifically for marketing/content-function roles, since it maps cleanly onto content-org pain points

7. **Draw conclusions the evidence actually supports.** Flag speculation as speculation. Don't manufacture a dramatic narrative if the listings are genuinely unremarkable — a thin signal is a valid finding.

8. **If the candidate's background was provided**, close with where their specific experience intersects with the identified pain points — not a generic "I'm a good fit" but a specific "here's the exact adjacent problem I've solved before."

## Output format

Markdown, structured roughly as:

```markdown
# Strategic Analysis: {Company} — {Role}

## What the listings reveal
[patterns across postings]

## The likely real priorities
[decoded pain points, with the language that signals each]

## Upstream / downstream context
[what's driving this, what's at stake]

## The hiring manager's likely position
[their probable goals and exposure]

## Relevant frameworks
[only the ones that added insight — briefly applied, not just named]

## Where this candidate's background intersects
[if background was provided]

## Sources
[endnote-style list of every URL used]
```

Always cite sources as an endnote list with URLs — don't leave claims about the company unsourced when they came from web research.
