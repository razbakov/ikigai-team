---
title: Customization
description: Rename agents, add projects, adjust boundaries — make it yours.
---

Everything is plain markdown files. Edit anything.

## Rename Agents

During setup, choose your own names. Or edit `.claude/agents/<name>.md` later — change the `name` field and rename the file. Update references in other agent files.

## Add Projects

Add to the project registry in `CLAUDE.md`:

```markdown
| my-new-project | `~/Projects/my-new-project` |
```

For projects with their own org, create a project agent — a thin router that hands off to the project's coordinator.

## Adjust OKRs

Edit the `## Current OKRs` section in each agent's file. Agents check their KRs before taking action.

## Change Boundaries

Edit the `## Boundaries` section. Keep it symmetric — if agent A says "hand off to B", make sure B's domain covers it.

## Add Skills

Install from the [skills repo](https://github.com/razbakov/skills):

```bash
claude install-skill https://github.com/razbakov/skills/tree/main/skills/<skill-name>
```

Then add it to the agent's `## Available Skills` section.

## Add Integrations

Configure MCP servers in Claude Desktop settings for:
- **Notion** — task boards, databases
- **GitHub** — issues, PRs, code review
- **Google Calendar** — scheduling
- **Figma** — design implementation
