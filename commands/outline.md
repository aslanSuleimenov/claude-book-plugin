---
description: Build or update the chapter-by-chapter plan with acts, turning points, and character arcs
---

Build a chapter-by-chapter outline for this book.

## Read first
1. `CLAUDE.md` — genre, mode, logline
2. `story/synopsis.md` — full story arc
3. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md` — structure models for this genre
4. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/genre-mechanics.md` — structural contracts
5. Any existing `story/plan.md` — build on it, don't replace unless asked
6. Existing chapters in `chapters/` — know what's already written

## Outline structure

For each chapter produce:
```
## Chapter NN — Title
**Act:** [act number or phase]
**POV:** [character if rotating]
**Scene(s):** [brief scene list]
**Goal:** [what the POV character wants]
**Conflict:** [what stands in the way]
**Outcome:** [what changes]
**Arc beat:** [which character arc this advances]
**Hook into next:** [what pulls reader forward]
```

## Act structure

Use the model appropriate for the genre:
- Three-act (most fiction, nonfiction narrative)
- Five-act (literary, epic)
- Hero's Journey beats (genre adventure, fantasy)
- Kishōtenketsu (for non-conflict structures)
- Freytag's pyramid (classical)

Mark turning points explicitly:
- Inciting incident
- Act breaks / midpoint
- Dark night / crisis
- Climax
- Resolution

## Character arcs

For each major character track want/need/internal contradiction across the outline. Note where their arc intersects with plot.

## Output

Write the outline to `story/plan.md`. If the file already exists, show the diff and confirm before overwriting.

After writing: report chapter count, estimated word count (chapters × avg chapter length), reading time.
