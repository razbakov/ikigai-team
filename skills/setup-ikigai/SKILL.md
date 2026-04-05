# Setup Ikigai Team

A guided journey to build your AI dream team. Starts with coaching, ends with a fully operational system.

## Trigger

- User says `/setup-ikigai`, "set up my ikigai team", "create my ikigai", or provides the GitHub repo URL

## Prerequisites

- Claude Desktop or Claude Code
- Claude Pro or Max subscription

## Philosophy

This is NOT a config wizard. It is a multi-session journey:

1. **Sage** helps the user reflect and find direction (L10L, GROW, mission)
2. **Marco** turns direction into strategy (OKRs)
3. **Maya** builds the daily rhythm (GTD)
4. The rest of the team forms around the user's goals

Each session saves progress. The user does not have to finish in one sitting.

## Process

### Session 1: Foundations (with Sage)

**Goal:** Get to know the user. Set up the org structure. Start the coaching journey.

**Step 1 — Quick setup questions:**
Ask these to create the workspace:
1. "What is your name?"
2. "Where should your organization live?" (default: `~/Orgs/ikigai`)

Generate the directory scaffold and agent files using templates from the ikigai-team repo. This creates the workspace so Sage has a place to save progress.

**Step 2 — Hand off to Sage for coaching:**

Sage runs a Level 10 Life assessment:
- Score 10 life areas (1-10): health, relationships, family, career, finances, personal growth, fun/recreation, physical environment, community, purpose
- Save the assessment to `assessments/`
- Reflect on the scores together

Ask the user: "How much time do you have today?" If they need to stop, save progress and schedule the next session. Otherwise continue to Session 2.

### Session 2: Find Direction (with Sage)

**Goal:** Define mission and vision using GROW.

Sage guides the user through the GROW framework:
- **Goal:** What do you want your life to look like? What is your ikigai?
- **Reality:** Your L10L scores. Where are the gaps?
- **Options:** What could you do? Brainstorm freely.
- **Way Forward:** Pick 2-3 things to focus on this quarter.

Save mission and vision to `profile.md`. Save the Way Forward.

Ask: "Ready to turn this into a strategy? Marco can help." If yes, continue. If not, schedule next session.

### Session 3: Strategy (with Marco)

**Goal:** Turn the Way Forward into OKRs.

Marco takes the Way Forward from Sage and helps define:
- 2-3 quarterly objectives
- 2-3 key results per objective
- How they map to projects

Ask about active projects:
- "What projects are you working on?" (name + path pairs)
- Generate project registry in CLAUDE.md

Save OKRs to each agent's file. Ask: "Ready to set up your daily rhythm?" If yes, continue.

### Session 4: Daily System (with Maya)

**Goal:** Set up GTD and daily reviews.

Maya introduces the daily rhythm:
- Morning: inbox processing, calendar review, daily plan
- During the day: dispatch to agents as needed
- Evening: scrum report
- Saturday: weekly review

Ask about integrations:
- "Do you want Telegram bots for mobile access?" (optional)
- "Do you use Notion for task management?" (optional)

Generate any integration config. Do initial commit:

```bash
cd {{org_path}}
git add -A
git commit -m "Initialize Ikigai Team"
```

Print: "Your team is ready. Open this folder in Claude Desktop and say 'Good morning Maya' to start your first day."

### Between Sessions

When saving progress between sessions:
1. Save current state to `.claude/agent-memory/setup/progress.md`
2. Note which session to resume (1, 2, 3, or 4)
3. Create a calendar event for the next session (if user provides a time)
4. Tell the user: "We saved your progress. When you are ready, open this folder and say 'Let us continue the setup.'"

When resuming:
1. Read `.claude/agent-memory/setup/progress.md`
2. Tell the user where they left off
3. Continue from that point

## Template Reference

Agent templates live in the ikigai-team repo under `templates/`:

| Role | Template |
|------|----------|
| ops | `templates/agents/chief-of-staff.md.hbs` |
| engineering | `templates/agents/cto.md.hbs` |
| content | `templates/agents/content-lead.md.hbs` |
| strategy | `templates/agents/strategy-lead.md.hbs` |
| coach | `templates/agents/personal-coach.md.hbs` |
| community | `templates/agents/community-lead.md.hbs` |
| project router | `templates/agents/project-router.md.hbs` |

## Output

- A fully scaffolded org directory with agent definitions and operational structure
- Completed Level 10 Life assessment
- Mission and vision in profile.md
- OKRs in each agent's file
- Ready to use: open folder in Claude Desktop, talk to Maya
