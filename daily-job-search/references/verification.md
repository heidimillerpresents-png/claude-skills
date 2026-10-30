# Verifying a posting is open

Read this during step 4. Each section gives the endpoint, what "open" looks like, and where the useful fields live.

## Greenhouse

- Feed URLs look like `https://job-boards.greenhouse.io/<board>/jobs/<id>` or `https://boards.greenhouse.io/<board>/jobs/<id>`.
- Check: `curl -sS -w "%{http_code}" https://boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>`
- **Open:** HTTP 200 with a JSON body. **Closed:** 404, or a redirect to the board's main page.
- Useful fields: `title`, `location.name`, `content` (HTML-escaped description; unescape it, then strip tags). Pay is usually near the end of `content`.
- Some companies host Greenhouse on their own domain (`company.com/careers?gh_jid=<id>`). The board API still works if you know the board name.

## Lever

- Feed URLs look like `https://jobs.lever.co/<company>/<id>`.
- Check: `curl -sS https://api.lever.co/v0/postings/<company>/<id>`
- **Open:** HTTP 200 with JSON. **Closed:** 404.
- Useful fields: `text` (title), `categories.location`, `categories.allLocations`, `descriptionPlain`, `lists` (requirements sections), `additionalPlain`, `salaryRange`.

## Ashby

- Feed URLs look like `https://jobs.ashbyhq.com/<company>/<id>`.
- Check: `curl -sS "https://api.ashbyhq.com/posting-api/job-board/<company>?includeCompensation=true"` and look for the job `id` in `jobs`.
- **Open:** the id is in the list. **Closed:** it is missing.
- Useful fields: `location`, `secondaryLocations`, `isRemote`, `workplaceType` (Remote, Hybrid, OnSite), `publishedAt`, `compensation.compensationTierSummary`, `descriptionPlain`.
- `publishedAt` changing on a role the candidate already applied to is a sign it was reposted.

## Workday

- Feed URLs look like `https://<tenant>.<wdN>.myworkdayjobs.com/<site>/job/<path>`.
- Check the JSON endpoint: `https://<tenant>.<wdN>.myworkdayjobs.com/wday/cxs/<tenant>/<site>/job/<path>`, where `<path>` is everything after `/job/` in the feed URL.
- **Open:** `canApply: true`. **Closed:** `canApply: false`, or an error.
- Some proxies block curl to Workday; use a web fetch tool instead.
- Useful fields: `jobPostingInfo.location`, `additionalLocations`, `remoteType`, `jobDescription` (pay is usually inside it), `startDate`, `endDate`.
- Watch for broken pay fields such as "1.00 to 225,000.25". Report them as unreadable rather than as a range.

## iCIMS

- Fetch the posting URL with `?in_iframe=1` added (or `&in_iframe=1` if it already has a query string).
- **Open:** the description and an "Apply for this job online" link render. **Closed:** a "no longer accepting applications" or similar notice.
- Page titles sometimes include a site-wide label such as "Work From Home". Don't treat that as the role's arrangement; look in the body.

## BambooHR, Paylocity, Jobvite, ApplicantPro and company career sites

- Fetch the posting page itself.
- **Closed** signs: "This position has been closed", a redirect to a support or "invalid job" page, "this job was removed", or a redirect to the generic careers page.
- Jobvite links that redirect to `jobvite.com/support/job-seeker-support/?invalid=1` are closed.

## Aggregators and job boards (leads only)

Indeed, LinkedIn, Built In, Wellfound, ZipRecruiter, Virtual Vocations, Mediabistro, Dice and similar sites are leads, never proof. Follow the lead to the employer's own posting and verify it there. Many aggregator pages stay up long after the role closes, and some say so in small print ("this job was removed at ...").
