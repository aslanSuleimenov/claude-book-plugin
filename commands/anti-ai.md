---
description: Scan for AI writing tells. No arg = full manuscript. With NN = single chapter.
argument-hint: "[NN]"
---

Scan for AI writing tells in $ARGUMENTS.

If no argument: scan all chapters in `chapters/`.
If NN given: scan only `chapters/NN_*.md`.

## Read first
1. `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`
2. Target chapter(s)

## Use the anti-ai-checker agent

Delegate the full scan to the `anti-ai-checker` agent.

## After the scan

If tells were found, ask the user:
> "Fix them now? I can rewrite the flagged passages — say `fix all`, `fix [pattern name]`, or point me to specific lines."

If the user says fix:
- Rewrite only the flagged passages
- Keep everything else untouched
- Show before/after for each change
- Save to the same chapter file
