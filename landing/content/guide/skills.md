---
title: Skills
description: Installable workflows that give each agent real capabilities.
---

Skills are reusable workflows your agents invoke with `/skill-name`. They are installed from the [skills repo](https://github.com/razbakov/skills).

## How It Works

```bash
claude install-skill https://github.com/razbakov/skills/tree/main/skills/daily-review
```

Then in any conversation:
```
/daily-review
```

Maya runs it. The skill orchestrates inbox processing, calendar review, and plan creation automatically.

## Skills by Agent

**Maya** — daily-review, weekly-review, process-inbox, scrum, suggest-tasks, dispatch-approved

**Viktor** — github-issue, sprint-planning, run-sprint, pr-review-responder, estimation, dependency-vuln-report

**Luna** — content-seo-agent, viral-threads, social-post, youtube-metadata-updater, brand-poster, image-from-gemini

**Marco** — product-coach, user-story, sales-bizdev-agent, freelance-job-hunt, storyteller-tactics, portfolio-hiring-analysis

**Sage** — personal-coach, year-review

**Kai** — agent-browser (contact research)

Browse all available skills on the [Skills page](/skills).
