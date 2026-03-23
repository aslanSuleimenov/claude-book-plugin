---
description: Initialize a new book project. Asks for mode, genre, POV. Optionally reads a draft file.
argument-hint: "[draft-file.md]"
---

Initialize a new book project in the current directory.

## Steps

**1. Read context**
If an argument was provided, read that file as the draft/synopsis.

**2. Ask the user (one message, all questions):**
- Mode: `from-scratch` (original prose) or `adapt` (screenplay → prose)?
- Book title (working title is fine)
- Genre (see craft/fiction/ or craft/nonfiction/ for options)
- POV: `third-limited` / `first` / `third-omniscient`
- Tense: `past` / `present`
- Brief logline or premise (1–2 sentences)
- If adapt mode: confirm they have screenplay scenes ready in source/

**3. Create project structure:**

Create these directories and files:
- `chapters/` — empty, will hold written chapters
- `source/` — (adapt mode) for screenplay scenes
- `bible/characters/` — character cards
- `bible/universe/` — locations, world rules
- `bible/structure.md` — acts, turning points, arcs (stub)
- `story/synopsis.md` — stub, ask user to fill
- `story/plan.md` — chapter-by-chapter plan (stub)
- `timeline/events.md` — chronology (append-only, stub)
- `state/current/situation.md` — last chapter + open threads (stub)
- `state/current/characters.md` — current character states (stub)
- `analytics/` — for research and reports
- `versions/` — for compiled DOCX
- `.work/` — temp agent reports (gitignore this)

**4. Write `CLAUDE.md`** in the project root using this template:

```markdown
# [TITLE]

## Project mode
mode: [from-scratch|adapt]

## Genre
genre: [genre]
genre-file: ${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md
genre-mechanics: ${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/genre-mechanics.md

## Prose parameters
POV: [third-limited|first|third-omniscient]
tense: [past|present]
compression: moderate
interiority: medium

## Story
logline: [logline]

## Style rules
- No AI writing tells — see ${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md
- Concrete image over abstract state
- Dialogue does not explain feelings
- No rule of three

## Notes
[Empty — user fills as project evolves]
```

**5. Confirm** — tell the user what was created, remind them:
- Fill in `story/synopsis.md` and `story/plan.md` before writing chapters
- Run `/outline` to build a chapter plan from their synopsis
- Run `/new-chapter 01 Title` (from-scratch) or `/convert 01` (adapt) to start writing
- Run `/type-check` to verify setup
