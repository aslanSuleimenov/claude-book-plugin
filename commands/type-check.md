---
description: Diagnostic — show mode, genre, compass status, chapter count
---

Run a diagnostic on this project.

## Check and report

Read `CLAUDE.md` and `chapters/`.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Project diagnostic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLAUDE.md:       [found / NOT FOUND]
Mode:            [from-scratch / adapt / not set]
Genre:           [value / not set]
Genre file:      [exists / MISSING]
Genre mechanics: [exists / MISSING]
POV:             [value / not set]
Tense:           [value / not set]

Chapters:        [N files in chapters/]
Story plan:      [story/plan.md exists / MISSING]
Synopsis:        [story/synopsis.md exists / MISSING]
State:           [state/current/situation.md exists / MISSING]

AI-tells file:   [${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md — exists / MISSING]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If any critical items are MISSING, explain what to do:
- No CLAUDE.md: run `/startproject`
- Mode not set: run `/startproject`
- Genre file missing: the genre may not be supported yet; check `${CLAUDE_PLUGIN_ROOT}/craft/`
- No story plan: run `/outline` or write `story/plan.md` manually
- No chapters: run `/new-chapter 01 Title` (from-scratch) or `/convert 01` (adapt)
