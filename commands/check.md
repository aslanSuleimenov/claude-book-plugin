---
description: Quality check. No arg = full. Types: style, continuity, characters, structure
argument-hint: "[style|continuity|characters|structure]"
---

Run quality check on this manuscript.

Argument: $ARGUMENTS

If no argument: run all four checks.
If argument given: run only that check type.

## style check
Use the `style-validator` agent.
Checks: POV breaks, tense breaks, forbidden patterns from CLAUDE.md, voice consistency, AI writing tells.
Output: `.work/check_style.md`

## continuity check
Use the `continuity-reviewer` agent.
Checks: timeline contradictions, geography errors, character knowledge (knows something they shouldn't), object tracking, name consistency.
Output: `.work/check_continuity.md`

## characters check
Use the `character-checker` agent.
Checks: voice consistency per character, behavioral consistency, arc progression, OOC moments.
Output: `.work/check_characters.md`

## structure check
Use the `structure-reviewer` agent.
Checks: pacing, act structure, open threads, scene balance, chapter length distribution.
Output: `.work/check_structure.md`

## Full check
Run all four agents. Then write a summary to `.work/check_full.md`:
- Critical issues (must fix before next chapter)
- Moderate issues (fix before final draft)
- Minor issues (polish pass)

Report to user: issue counts by severity, files written.
