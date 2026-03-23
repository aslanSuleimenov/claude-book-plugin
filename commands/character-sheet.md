---
description: Generate or update a character card with arc, voice, wants/needs/contradictions
argument-hint: "Name"
---

Create or update a character sheet for $ARGUMENTS.

## Read first
1. `CLAUDE.md` — genre, mode
2. Any existing `bible/characters/[name].md`
3. All chapters in `chapters/` — scan for this character's appearances
4. `state/current/characters.md` — current state
5. `story/synopsis.md` — their role in the story

## Character sheet structure

Write to `bible/characters/[name-lowercase].md`:

```markdown
# [Full Name]

## Identity
- **Role:** [protagonist / antagonist / supporting / etc.]
- **Age:**
- **Appearance:** [brief, distinctive — not a mirror scene]

## Psychology
- **Want:** [what they consciously pursue]
- **Need:** [what they actually need — often different from want]
- **Fear:** [what drives their avoidance]
- **Wound:** [the backstory event that shaped them]
- **Lie they believe:** [their false worldview]
- **Truth they need to learn:**

## Voice
- **Speech patterns:** [sentence length, vocabulary, verbal tics, what they avoid saying]
- **Internal voice:** [how they think — cynical, poetic, tactical, etc.]
- **Tells:** [physical behaviors when stressed, lying, happy]

## Arc
| Phase | Belief | Behavior |
|-------|--------|----------|
| Start | | |
| Midpoint | | |
| Dark night | | |
| End | | |

## Relationships
- [Character A]: [dynamic]
- [Character B]: [dynamic]

## Appearances
[Auto-filled from chapter scan: Chapter NN — brief note]

## Notes
```

If the character already has a file, update it rather than replacing — note what changed and why.
