---
description: Find continuity errors across the manuscript or a chapter range
argument-hint: "[NN-MM | NN]"
---

Check continuity for $ARGUMENTS.

If no argument: check full manuscript.
If range NN-MM: check only those chapters.
If single NN: check that chapter against all previous chapters.

## Read first
1. `CLAUDE.md`
2. Target chapters from `chapters/`
3. `timeline/events.md`
4. `bible/characters/*.md`
5. `bible/universe/*.md`
6. `state/current/situation.md` and `state/current/characters.md`

## What to check

### Timeline
- Stated times and dates — do they add up?
- Travel times — realistic for the world?
- "Next morning" / "three days later" — do the counts match?
- Season/weather — consistent with timeline?

### Geography
- Characters moving between locations — is the distance/time plausible?
- Room layouts — consistent across scenes?
- Directions (left, right, north) — consistent?

### Character knowledge
- Does a character know something they weren't present for and nobody told them?
- Does a character forget something they know?
- Is a secret revealed too early or still kept when it shouldn't be?

### Objects and details
- Weapon/tool continuity (loaded, unloaded, where it was put down)
- Physical injuries — do they persist appropriately?
- Props introduced and not resolved (Chekhov's gun problems)
- Names spelled consistently?
- Eye color, hair, physical description — consistent?

## Output

Print findings grouped by type. For each issue:
```
[Chapter NN, ~paragraph X] ISSUE TYPE
Problem: [description]
Evidence: "[quote or paraphrase from text]"
Conflicts with: [Chapter MM or timeline/characters/bible reference]
Suggested fix: [brief]
```

Save full report to `.work/continuity_[date].md`.
