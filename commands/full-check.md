---
description: Full manuscript audit. Runs all 10 specialized checkers in optimal order (foundation → characters → structure → reader). Produces consolidated dashboard with priority fixes.
argument-hint: "[NN | NN-MM]"
---

# /full-check

Run complete manuscript quality audit using all 10 specialized checkers.

## Usage

```
/full-check              # Analyze all chapters
/full-check 5            # Analyze chapter 5 only
/full-check 3-7          # Analyze chapters 3–7
```

## What It Does

Orchestrates 10 checkers in 5 phases. Each phase builds on the previous.

**Phase 1 — Foundation** *(must pass before continuing)*
- `continuity-checker` — plot and character continuity across chapters
- `timeline-checker` — chronological consistency, travel logic, time arithmetic
- `consistency-checker` — world rules, setting facts, internal contradictions

**Phase 2 — Characters**
- `ooc-checker` — out-of-character behavior, speech pattern violations
- `voice-checker` — narrative voice and POV consistency

**Phase 3 — Structure**
- `outline-checker` — prose adherence to story/plan.md
- `pacing-checker` — scene type balance, action/emotion/world-building rhythm

**Phase 4 — Reader Experience**
- `prose-checker` — line-level craft: pacing, show/tell, dialogue subtext
- `high-point-checker` — satisfaction moment density and quality
- `reader-pull-checker` — chapter hooks, micro-payoffs, reading momentum

**Phase 5 — Synthesis**
- Consolidates all 10 reports into `analytics/full-check-dashboard.md`
- Prioritizes fixes by impact
- Flags critical issues that must be resolved before next chapter

## Output

Creates 11 files in `analytics/`:

- `full-check-dashboard.md` — **main report (start here)**
- `check_01_continuity.md`
- `check_02_timeline.md`
- `check_03_consistency.md`
- `check_04_ooc.md`
- `check_05_voice.md`
- `check_06_outline.md`
- `check_07_pacing.md`
- `check_08_prose.md`
- `check_09_highpoints.md`
- `check_10_readerpull.md`

## Execution Rules

⚠️ **MODEL: Switch to Haiku before running this command. Announce switch and wait for user confirmation.**

- Phase 1 is a **gate** — if all three foundation checkers fail with critical issues, pause and report before continuing
- Checkers within the same phase run **sequentially** (not parallel) to preserve context window
- All reports are **permanent** in analytics/ (not .work/ — full-check is archival)
- Always run to completion unless user explicitly stops

## Dashboard Format

```
═══════════════════════════════════════════════════════════
FULL MANUSCRIPT CHECK — DASHBOARD
Manuscript: [title from CLAUDE.md]
Genre: [genre]
Chapters: [range checked]
Date: [date]
═══════════════════════════════════════════════════════════

⚠️ CRITICAL ISSUES (fix before writing next chapter)
────────────────────────────────────────────────────────
[If none: "No critical issues found."]

1. [Issue] — Source: [checker]
   Chapter [X]: [Detail]
   Fix: [Specific action]

🔴 PRIORITY FIXES (fix before final draft)
────────────────────────────────────────────────────────
1. [Issue] — [checker]
2. [Issue] — [checker]

🟡 SUGGESTIONS (polish pass)
────────────────────────────────────────────────────────
1. [Issue] — [checker]

PHASE RESULTS
────────────────────────────────────────────────────────
Phase 1 - Foundation: [✓ PASS / ⚠️ ISSUES / ✗ CRITICAL]
Phase 2 - Characters: [✓ PASS / ⚠️ ISSUES]
Phase 3 - Structure:  [✓ PASS / ⚠️ ISSUES]
Phase 4 - Reader:     [✓ PASS / ⚠️ ISSUES]

CHECKER SUMMARY
────────────────────────────────────────────────────────
| Checker              | Critical | High | Medium | Low |
|----------------------|----------|------|--------|-----|
| continuity-checker   | 0        | 1    | 2      | 0   |
| timeline-checker     | 0        | 0    | 1      | 0   |
| consistency-checker  | 0        | 0    | 0      | 0   |
| ooc-checker          | 0        | 1    | 0      | 2   |
| voice-checker        | 0        | 0    | 3      | 0   |
| outline-checker      | 0        | 0    | 1      | 0   |
| pacing-checker       | 0        | 1    | 0      | 0   |
| prose-checker        | 0        | 0    | 2      | 4   |
| high-point-checker   | 0        | 0    | 1      | 0   |
| reader-pull-checker  | 0        | 1    | 0      | 0   |

VERDICT
────────────────────────────────────────────────────────
[2-3 sentence overall assessment]

Next steps:
1. [Top priority]
2. [Second priority]
3. [Third priority]
```

## Notes

- Agents run in **dependency order** (foundation errors affect everything else)
- Phase 1 Foundation gate: pause if continuity/timeline/consistency have CRITICAL issues
- Reports in `analytics/` — permanent record of manuscript state at this checkpoint
- Use `/check [name]` for targeted single-agent runs between full checks
- Full check is designed as a **milestone tool** (before major revision, before submitting)

## See Also

- `/check [checker-name]` — single targeted checker
- `/analyze` — prose analysis (different focus: structure, genre, AI patterns)
- `/continuity` — quick continuity scan (lighter than full-check)
