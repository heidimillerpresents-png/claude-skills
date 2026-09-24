---
name: linkedin-profile-review
description: Reviews a LinkedIn profile and gives prioritized, actionable feedback for a job search — checking experience-section date errors, photo/cover photo, headline, bullet quality, and connection count. Use this whenever the user pastes in LinkedIn profile content (About section, experience history, headline) and/or a profile photo and asks for feedback, a review, an audit, or help before they start applying to jobs — even if they don't use the word "skill" or "audit" explicitly. Also trigger if the user is helping someone else (e.g. a laid-off colleague, a friend, a client) review their LinkedIn profile. Do NOT trigger for resume/cover letter review (that's a separate task) or for general job-search strategy questions with no profile content provided.
---

# LinkedIn Profile Review

Gives a prioritized, no-fluff critique of a LinkedIn profile aimed at improving how the person reads to recruiters and how often they surface in recruiter search.

## Critical constraint: no live LinkedIn access

Claude cannot browse to LinkedIn URLs — LinkedIn blocks unauthenticated/scraped access, and there is no LinkedIn connector by default. This skill works **only from what the user pastes or uploads**: profile text (About, headline, experience bullets, connection count) and/or an uploaded photo.

If the user only provides a bare LinkedIn URL with no pasted content, tell them plainly that you can't open it and ask them to paste the relevant sections (headline, About, Experience, and a screenshot or description of the photo/banner) instead. Don't guess at content you weren't given.

If a browser-automation tool (e.g. Claude for Chrome, or an MCP connector) IS available in this session, it's fine to use it to fetch the live page — but never assume it's there. Check the tool list first.

## What to review, in order

Work through these checks. Skip a section if the user didn't provide the relevant content (e.g. no photo uploaded = skip the photo section, don't invent a description of it).

### 1. Experience section integrity (usually the highest-priority fix)
- Look for overlapping or unclosed date ranges — e.g. two "Present" roles at the same company, or a promotion where the old role's end date wasn't set. This is the single most common and most damaging LinkedIn error: it reads as a data-entry mistake at best, and dishonest at worst.
- Look for multiple distinct jobs/employers crammed into one position's description instead of being split into separate entries with their own dates. This is common when someone pastes an old resume's full history into a single LinkedIn bullet.
- Flag any date math that doesn't add up.

### 2. Photo
- Sunglasses, hats, outdoor/recreational gear, group photos, or casual settings all undercut a professional title. Recruiter guidance and LinkedIn's own data consistently flag no-eye-contact and non-professional settings as trust/approachability negatives.
- Recommend a plain, well-lit, front-facing headshot with a neutral background — note this is a fast phone-camera fix, not something that requires a professional photographer, so the suggestion is actionable.

### 3. Cover/banner photo
- Flag if missing (default blank banner reads as neglect). Suggest something cheap and fast: a simple text banner with their specialty/keywords, or an employer-branded image if appropriate.

### 4. Headline
- If it's just the job title, that's wasted real estate. Recommend reworking it to front-load searchable keywords (skills, specialties, domain) rather than only the title — this is what recruiters and LinkedIn search actually index on.
- If the person is job-searching and their headline still reads as fully tied to a current/former employer in a way that could confuse recruiters, flag it.

### 5. Bullet/description quality
- Distinguish bullets that describe *scope of responsibility* ("Directed creation of...", "Managed...") from ones that describe *outcomes* (time saved, cost reduced, adoption increased, revenue influenced). Flag responsibility-only bullets and suggest they get quantified, even with rough estimates, since outcome language is what differentiates a candidate.

### 6. Connections
- Note if the connection count looks thin relative to their years of experience and number of employers (a rough gut-check, not a hard formula — use judgment: someone with 10+ years across multiple companies with under ~500 connections is worth flagging). Low connection count can suppress how often someone surfaces in recruiter searches. Suggest connecting with former colleagues across their listed employers before actively applying.

## Output format

Give a ranked list (not a wall of prose) ordered by what's actually costing the person the most — usually: factual/date errors first (they look like mistakes or red flags), then photo, then headline/positioning, then bullet content, then connections. For each item: what's wrong, why it matters (be concrete about how a recruiter reads it), and the specific fix. Close with a one-line priority order if the list is long.

Keep the tone direct and evaluative, not just descriptive — this skill exists to tell the person what to fix, not just to summarize their profile back to them.
