---
description: Renumber all chapters sequentially (two-phase rename to avoid collisions)
---

Renumber all chapter files in `chapters/` sequentially starting from 01.

## Read first
List all files in `chapters/` sorted by current number prefix.

## Show plan first

Before renaming, show the user:
```
Current → New
  01_intro.md              → 01_intro.md (unchanged)
  02_the-meeting.md        → 02_the-meeting.md (unchanged)
  02b_extra-scene.md       → 03_extra-scene.md
  04_aftermath.md          → 04_aftermath.md (unchanged)
  ...

Proceed? [y/n]
```

Wait for confirmation.

## Two-phase rename (Windows-safe)

Phase 1: Rename all files to temp names to avoid collisions.
```
chapters/01_intro.md → chapters/tmp_001_intro.md
chapters/02_the-meeting.md → chapters/tmp_002_the-meeting.md
...
```

Phase 2: Rename from temp to final names.
```
chapters/tmp_001_intro.md → chapters/01_intro.md
chapters/tmp_002_the-meeting.md → chapters/02_the-meeting.md
...
```

## Rules
- Only whole numbers (01, 02, 03...) — no letters or suffixes
- Two-digit padding up to 99, three-digit for 100+
- Preserve the title part of the filename (everything after NN_)
- Non-chapter files in chapters/ (e.g., README.md) are skipped

## After renumber

Report: "Renumbered N chapters. No files were deleted."
