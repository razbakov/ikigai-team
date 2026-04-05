# Setup Ikigai Team

Set up your AI dream team using Ikigai Team. Creates an org directory with S3 governance, agent definitions, operational workflows, and optional Telegram bot infrastructure.

## Trigger

- User says `/setup-ikigai`, "set up agent team", "create my ikigai", "install ikigai framework"

## Prerequisites

- Claude Code installed and authenticated
- Git available
- The ikigai-team repo cloned locally (or accessible via GitHub)

## Process

### Phase 1: Discovery

Ask the user these questions one at a time. Accept defaults in parentheses if the user presses enter.

1. **"What is your name?"** — Full name for agent prompts. Store as `owner_name`. Extract first name as `owner_first_name`.

2. **"Where should your organization live?"** — Default: `~/Orgs/ikigai`. This is the governance/ops layer, not code. Store as `org_path`.

3. **"Where should media files live? (large files, recordings, NOT in git)"** — Default: `~/Local/<org-name>`. Store as `media_path`.

4. **"What is your GitHub repo for issue tracking?"** — e.g., `username/ikigai`. Store as `github_repo`. Set `issue_tracker` to `GitHub Issues (repo: {{github_repo}})`.

5. **"What is your mission? (one sentence)"** — Seeds the README. Store as `mission`.

6. **"Name your agents or use defaults?"**
   
   The dream team defaults:
   | Role | Name | Personality |
   |------|------|------------|
   | Chief of Staff | **Maya** | ISTJ — reliable, systematic |
   | CTO | **Viktor** | INTJ — strategic, efficient |
   | Content & Growth | **Luna** | ENFP — imaginative, enthusiastic |
   | Strategy & Business | **Marco** | ENTJ — analytical, decisive |
   | Personal Coach | **Sage** | INFJ — insightful, empathetic |
   | Community & Partnerships | **Kai** | ESFJ — warm, connector-minded |
   
   If the user wants custom names, ask for each role. Store each as `agent_<role>_name` and `agent_<role>_name_lower` (lowercase).

7. **"Do you want Telegram bot integration? (y/n)"** — Default: `n`. Store as `use_telegram`.
   
   If yes, ask:
   - "What is your Telegram user ID?" — Store as `telegram_user_id`
   - For each agent: "Bot username for <name>?" — e.g., `@maya_raz_bot`. Store as `agent_<role>_bot_username`.
   - Token env var names are auto-generated: `<NAME>_BOT_TOKEN`

8. **"Do you want Notion integration? (y/n)"** — Default: `n`. Store as `use_notion`.

9. **"List your active projects (or skip to add later)."**
    
    Format: `name, path` per line. Example:
    ```
    WeDance, ~/Orgs/WeDance
    my-app, ~/Projects/my-app
    ```
    Store as `projects` array of `{name, path}`.

10. **"What are your top 2 OKRs this quarter? (or skip)"**
    
    Example:
    ```
    O1: Prove WeDance can be a business
    O2: Build a reliable system for side-project progress
    ```
    Store as `okr_1`, `okr_2`. If skipped, use placeholders.

### Phase 2: Generation

After collecting all answers, generate the organization structure.

#### Step 1: Create directory scaffold

```
{{org_path}}/
  .claude/
    agents/           # Agent definitions (generated next)
    agent-memory/     # Persistent memory per agent
  ops/
    sessions/         # Daily logs
    inbox/            # Processed inbox files
    reviews/          # Weekly reviews
  contacts/           # CRM
  strategy/
    decisions/        # Decision log
    experiments/      # Hypothesis tracking
  assessments/        # Level 10 Life snapshots
  output/             # Generated artifacts
  .bin/               # Scripts (if Telegram enabled)
```

Create each directory with `mkdir -p`. Initialize git in `{{org_path}}`.

#### Step 2: Generate CLAUDE.md

Read `templates/CLAUDE.md.hbs` from the ikigai-team repo. Substitute all `{{variables}}` with collected values. Handle conditional sections:
- Remove `{{#if use_telegram}}...{{/if}}` blocks if `use_telegram` is false
- Remove `{{#if use_notion}}...{{/if}}` blocks if `use_notion` is false
- Expand `{{#each}}` loops for projects and agents

Write the result to `{{org_path}}/CLAUDE.md`.

#### Step 3: Generate agent files

For each of the 6 agent roles:

1. Read the corresponding template from `templates/agents/<role>.md.hbs`
2. Substitute all variables
3. Build the Team section dynamically (list all OTHER agents, not self)
4. Build the project agents section if any projects have org-level routing
5. Write to `{{org_path}}/.claude/agents/{{agent_name_lower}}.md`

Template mapping:
| Role | Template |
|------|----------|
| ops | `chief-of-staff.md.hbs` |
| engineering | `cto.md.hbs` |
| content | `content-lead.md.hbs` |
| strategy | `strategy-lead.md.hbs` |
| coach | `personal-coach.md.hbs` |
| community | `community-lead.md.hbs` |

For each project that has an org path (`~/Orgs/*`), also generate a project router agent using `project-router.md.hbs`.

#### Step 4: Generate profile templates

Write `{{org_path}}/profile.md` and `{{org_path}}/now.md` from their respective templates.

#### Step 5: Generate README

Write `{{org_path}}/README.md` with mission, agent table, and structure overview.

#### Step 6: Initial commit

```bash
cd {{org_path}}
git add -A
git commit -m "Initialize ikigai framework with the dream team"
```

### Phase 3: Skill Recommendations

Print recommended skills to install for each agent. See `docs/skills-catalog.md` for the full list per role.

### Phase 4: Verification

Run these checks:
1. Confirm `{{org_path}}/CLAUDE.md` exists and is non-empty
2. Confirm all agent files exist in `.claude/agents/`
3. Confirm agent YAML frontmatter parses correctly
4. Confirm directory scaffold exists
5. Confirm git repo initialized with initial commit

Print summary with next steps.

## Output

- A fully scaffolded org directory with agent definitions, CLAUDE.md, and operational structure
- Ready to use immediately with `claude --agent <name>`
