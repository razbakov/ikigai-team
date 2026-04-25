## Content & Publishing

Generic publishing rules. Per-domain rules (which languages to translate to, which platforms to cross-post to, your specific URL structure) belong in your private CLAUDE.md.

### Visual assets

- **Hero images** for blog posts and long-form content must be generated using `/image-from-gemini`. Never copy thumbnails from other sources or reuse stock images for primary hero positions.
- **YouTube thumbnails** must be Gemini-generated, not HTML-rendered. HTML + headless Chrome thumbnails look generic and hurt click-through. The paired blog post's hero image is usually the right source if it exists; otherwise generate a new one with Gemini.
- Resize thumbnails to 1280px wide with `sips --resampleWidth 1280` before uploading.

### Cross-posting

- DEV.to posts must include `canonical_url` in frontmatter pointing back to the original.
- Each cross-post platform has its own metadata requirements — document them in the per-domain rules of your private repo, not here.

### Frontmatter discipline

- All `last_updated` / `updated_at` fields must be actual datetimes (e.g. `2026-04-07 02:30`), never relative phrases like "today" or "just now". Future readers (including agents) cannot resolve relative timestamps.

### After deployment, update CLAUDE.md

After any deployment or URL change, update the relevant CLAUDE.md (PostHog table, Project Path Registry, deploy notes — wherever the URL is canonicalised) before reporting done. Stale URL references cascade into broken playbooks.

### Vercel auto-deploy is mandatory

When deploying to Vercel, always connect the GitHub repo and ensure auto-deploy on push works. Verify by pushing a commit and confirming the build succeeds remotely. Never leave a project relying on manual `vercel deploy` only — manual deploys silently rot.
