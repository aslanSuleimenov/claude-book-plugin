---
description: Rewrite a chapter with notes
argument-hint: "NN notes"
---

Rewrite chapter $ARGUMENTS.

Parse: first token is chapter number NN, rest is rewrite notes/instructions.

## Read first
1. `CLAUDE.md` — all style parameters
2. `chapters/NN_*.md` — the current chapter (read it fully)
3. `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`
4. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md`
5. Adjacent chapters (prev/next) for continuity
6. Relevant `bible/characters/*.md`

## Rewrite process

**Understand the notes first.** Don't start rewriting until you know what the user wants changed. If the notes are ambiguous, ask one clarifying question.

Types of rewrites:
- **Tone/voice** — adjust prose register, sentence rhythm, interiority level
- **Scene restructure** — change order, pacing, what's shown vs. told
- **Character fix** — voice inconsistency, OOC behavior
- **Continuity fix** — timeline, geography, knowledge errors
- **AI-pattern removal** — strip tells, replace with concrete images
- **Compression** — cut to tighten
- **Expansion** — add texture, interiority, subtext

**Preserve what works.** Don't rewrite sections that aren't covered by the notes.

## Output

Save to the same `chapters/NN_*.md` file. The old version is in git history.

Report:
- Word count before/after
- What changed and why
- Any continuity implications for other chapters
