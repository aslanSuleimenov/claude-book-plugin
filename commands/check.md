---
description: Quality check. No arg = full 11-agent audit. Named checker = single agent. Group = style/continuity/characters/structure/pacing
argument-hint: "[checker-name|group|all]"
---

Run quality check on this manuscript.

Argument: $ARGUMENTS

## Available checkers (by name)

Call any single checker directly:

| Checker | What it does |
|---------|-------------|
| `continuity-checker` | Plot and character continuity across chapters |
| `outline-checker` | Prose adherence to plan.md |
| `prose-checker` | Line-level craft: pacing, show/tell, dialogue |
| `timeline-checker` | Chronological consistency, time logic |
| `voice-checker` | Narrative voice and style consistency |
| `consistency-checker` | Setting, world rules, internal facts |
| `ooc-checker` | Out-of-character behavior detection |
| `pacing-checker` | Scene type balance, rhythm |
| `high-point-checker` | Satisfaction moment density |
| `reader-pull-checker` | Chapter hooks and reading momentum |

Also available (original agents):

| Checker | What it does |
|---------|-------------|
| `style` | POV, tense, forbidden patterns (style-validator agent) |
| `continuity` | Timeline, geography, knowledge errors (continuity-reviewer agent) |
| `characters` | Voice and behavior consistency (character-checker agent) |
| `structure` | Pacing, acts, arcs, open threads (structure-reviewer agent) |

## Single checker

If argument matches a checker name: run that agent, output to `.work/check_[name].md`

## Group check (legacy)

- `style` → style-validator
- `continuity` → continuity-reviewer
- `characters` → character-checker
- `structure` → structure-reviewer

## Full check (no argument or `all`)

⚠️ SWITCHING TO HAIKU — This runs 11 lightweight checkers sequentially.
Switch to Haiku model now for token efficiency. Wait for user to confirm model switch before proceeding.

Run agents in this order (each writes to `.work/`):

**Phase 1: Foundation (most critical)**
1. `continuity-checker` → `.work/check_01_continuity.md`
2. `timeline-checker` → `.work/check_02_timeline.md`
3. `consistency-checker` → `.work/check_03_consistency.md`

**Phase 2: Character**
4. `ooc-checker` → `.work/check_04_ooc.md`
5. `voice-checker` → `.work/check_05_voice.md`

**Phase 3: Structure & Pacing**
6. `outline-checker` → `.work/check_06_outline.md`
7. `pacing-checker` → `.work/check_07_pacing.md`

**Phase 4: Reader Experience**
8. `prose-checker` → `.work/check_08_prose.md`
9. `high-point-checker` → `.work/check_09_highpoints.md`
10. `reader-pull-checker` → `.work/check_10_readerpull.md`

After all 10 agents complete, write `.work/check_full_summary.md`:

```
# Full Check Summary
Date: [date]
Chapters checked: [range]

## Critical Issues (fix before next chapter)
[list from all agents]

## High Priority (fix before final draft)
[list from all agents]

## Suggestions (polish pass)
[list from all agents]

## Per-Checker Status
| Checker | Issues | Warnings | Status |
|---------|--------|----------|--------|
| continuity-checker | N | N | ✓/⚠️/✗ |
| timeline-checker | ... |
...

## Recommendation
[overall verdict and top 3 priorities]
```

Report to user: issue counts by checker, files written, top priorities.
