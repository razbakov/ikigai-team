## Daily Review

The daily review is the heartbeat of the operating system. It's how nothing falls through cracks.

### File locations

- **Daily reviews** → `ops/sessions/YYYY-MM-DD-daily-review.md`
- **Weekly reviews** → `ops/reviews/YYYY-MM-DD-weekly-review.md`
- **Telegram inbox dumps** → `ops/inbox/YYYY-MM-DD-HH-MM.md`

The daily review only **links to** inbox files — it doesn't inline them.

### What the daily review must include

- Check the last weekly review for missed priorities.
- Process Chrome bookmarks as a GTD inbox.
- Check the dispatch surface (Butler / equivalent) for agent messages during inbox processing.
- A meal plan for lunch and dinner. Use the `/meal-suggestion` skill.
- Reasoning for the day's priorities at the end (one paragraph: why these, why now, what gets dropped).

### Daily Check-in calendar event

- Must include deep links: dispatch surface URL, Telegram chat link, session file path.
- The `/daily-standup` skill must schedule the standup agenda via the dispatch surface before sending the morning DM.

### Schedule

- Data gathering at **6am** (background — agent collects context).
- Morning DM from Maya at exactly **9:00**.
- Always sync the daily plan to Google Calendar without asking permission.

### File first, message second

When producing strategic summaries, save the file before sending the message. The message should link to the file, not contain it. This protects long-form thinking from getting buried in chat scrollback.

### Other recurring processes

- Inbox processing from the dispatch surface runs **hourly**.
- Sessions live in `ops/sessions/`. Three types:
  - **Browser history** (`YYYY-MM-DD-browser.md`) — Chrome History SQLite → time-block summary
  - **AI transcripts** (`YYYY-MM-DD-ai-sessions.md`) — Claude session JSONL + Conductor DB → project groups
  - **Other** (`YYYY-MM-DD-topic.md`) — check-ins, working sessions, focused topics
