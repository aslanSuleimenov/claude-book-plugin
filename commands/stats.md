---
description: Chapter count, word count, reading time, prose type breakdown
---

Show manuscript statistics.

## Read
1. `CLAUDE.md` — title, mode, genre
2. All files in `chapters/` — read each one

## Calculate

For each chapter:
- Word count (approximate: split on whitespace)
- Identify prose types (rough percentage):
  - Narrative/description
  - Dialogue
  - Internal monologue/interiority

For the full manuscript:
- Total chapters
- Total words
- Reading time (250 words = 1 minute)
- Average chapter length
- Longest / shortest chapter

## Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Book Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Chapters:     NN
Total words:  NN,NNN
Reading time: ~N hr NN min

Chapter breakdown:
  01 — Title        N,NNN words
  02 — Title        N,NNN words
  ...

Average chapter:  N,NNN words
Longest:  NN — Title (N,NNN)
Shortest: NN — Title (N,NNN)

Prose mix (approximate):
  Narrative:    NN%
  Dialogue:     NN%
  Interiority:  NN%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Note: word count is approximate. For precise count use a dedicated word processor.
