# linkedin-profile-review

A Claude Skill that reviews a LinkedIn profile and returns prioritized, actionable feedback for a job search: experience-section date errors, photo/cover photo, headline, bullet quality, and connection count.

## Important: no live LinkedIn access

Claude cannot browse to LinkedIn URLs — this skill works from **pasted profile content and/or an uploaded photo**, not from a URL. Paste in the headline, About section, experience history, and connection count, and attach a screenshot if you want the photo reviewed.

## Install

**Claude Code / CLI agents** — clone and drop into your skills directory:
```bash
git clone https://github.com/<your-username>/linkedin-profile-review.git
cp -r linkedin-profile-review ~/.claude/skills/
```
or, project-local:
```bash
cp -r linkedin-profile-review .claude/skills/
```

**Claude.ai / API** — upload `SKILL.md` (or the packaged `.skill` file) directly wherever your Claude client supports skill uploads.

## Use

Paste a profile's content (and a photo, if you want it critiqued) and ask for a review, feedback, or an audit. The skill triggers automatically on that pattern — no special phrasing needed.

## License

MIT — use, copy, adapt.
