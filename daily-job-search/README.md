# Daily Job Search (Claude skill)

A Claude skill that runs a verified daily job search for one person. It pulls fresh postings from a job feed, adds a web search pass for contract roles, filters them to your lanes and location rules, removes roles you already applied to, confirms each one is open on the employer's own site, ranks the fit, matches your LinkedIn connections, and publishes a shortlist.

It never applies to jobs, drafts resumes or sends outreach. It finds and vets roles; you decide what to do with them.

## What's in the folder

| File | What it does |
| --- | --- |
| `SKILL.md` | The skill: your profile, the run steps, and common pitfalls |
| `references/verification.md` | How to check whether a posting is open on Greenhouse, Lever, Ashby, Workday, iCIMS and other career sites |
| `scripts/pull_feed.py` | Downloads a chunked job feed in parallel, retries bad chunks, and filters by age and title keywords |

## Set it up

1. Open `SKILL.md` and replace every `{{CUSTOMIZE: ...}}` placeholder: your profile, lanes, pay floor, location rules, title keywords, job feed, tracker, connections export, where to publish, and your writing rules. Each placeholder includes an example.
2. Export your LinkedIn connections (LinkedIn: Settings, Data privacy, Get a copy of your data, Connections) and put the CSV somewhere Claude can read it.
3. Keep an application tracker with at least Company, Title, Applied and Status columns.
4. Add the folder to Claude as a skill (zip it, or upload `SKILL.md` and the folders where your Claude app allows skills).

## Run it

Ask Claude something like "run my daily job search". To run it every morning, set it up as a scheduled task and tell the scheduled prompt to use this skill.

## Requirements

- A shell with `curl` and Python 3 (standard library only)
- Web search and web fetch tools for the contract pass and Workday or iCIMS checks
- Access to your tracker and connections file (for example, a Google Drive connector)
- Somewhere to publish the shortlist (a page, a doc, or a file)

## About the job feed

The example feed in `SKILL.md` is a public, community-maintained dataset that covers Workday, iCIMS, Greenhouse, Paylocity, Lever, BambooHR and Ashby postings. Check its terms before relying on it, and swap in your own source if you prefer. If your feed has a different shape, adapt the loading section of `scripts/pull_feed.py`.

## License

See the `LICENSE` file at the top of the claude-skills repository.
