---
description: Update world state after chapter NN
argument-hint: "NN"
---

Update the world state after chapter $ARGUMENTS.

## Read first
1. `chapters/NN_*.md` — the chapter to process
2. `state/current/situation.md` — current state to update
3. `state/current/characters.md` — current character states to update
4. `timeline/events.md` — chronology to append to
5. Relevant `bible/characters/*.md` for characters in the chapter

## Update situation.md

Replace content with:
```markdown
# Current Situation (after Chapter NN)

## Last chapter summary
[2–4 sentence summary of what happened]

## Open threads
- [Thread 1: brief description, when introduced]
- [Thread 2: ...]

## Setting
[Where we are at chapter end: location, time of day, immediate context]

## Immediate next
[What the reader expects will happen next — the pull forward]
```

## Update characters.md

For each character who appeared or was affected:
```markdown
## [Character Name]
- **Location:** [where they are]
- **Physical state:** [injuries, fatigue, appearance changes]
- **Emotional state:** [what they're feeling — concrete, not labeled]
- **Knowledge:** [what they now know that they didn't before]
- **Relationships:** [any changed relationships]
- **Arc position:** [where they are in their arc]
```

## Append to timeline/events.md

Add a block:
```markdown
## Chapter NN — [Title] — [In-story date/time if known]
- [Event 1]
- [Event 2]
...
```

Do not rewrite existing timeline entries — append only.

## Confirm

Report to user: what was updated, any continuity flags noticed while reading the chapter.
