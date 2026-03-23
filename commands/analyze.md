---
description: Full manuscript analysis, or single chapter with NN argument
argument-hint: "[NN]"
---

Analyze $ARGUMENTS.

If no argument: full manuscript analysis.
If NN given: analyze only chapter NN.

## Read first
1. `CLAUDE.md`
2. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md`
3. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/genre-mechanics.md`
4. `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`
5. Target chapter(s) from `chapters/`
6. `story/plan.md` and `story/synopsis.md`

## Analysis dimensions

### 1. Structure
- Act structure compliance
- Pacing (scene length, chapter length distribution)
- Scene-level: goal / conflict / outcome per scene
- Open threads: raised vs. resolved
- Midpoint, turning points — present and functional?

### 2. Genre contracts
- Promise: set in chapter 1? Honored?
- Must-happen beats: present?
- Forbidden elements: any violations?

### 3. Prose quality
- POV consistency
- Tense consistency
- Interiority vs. action balance (matches setting in CLAUDE.md?)
- Sentence rhythm variety
- Show vs. tell ratio

### 4. AI writing tells
Check against `avoid-ai-writing-tells.md`:
- Rule of three
- Emotional placeholders
- Dialogue that explains feelings
- Abstract states instead of concrete images
- Any other flagged patterns

List specific instances with line references.

### 5. Character
- Voice consistency per character
- Arc progression vs. plan
- Want/need/contradiction visible in behavior?

## Output format

For full manuscript: `analytics/analysis_[date].md`
For single chapter: print to screen.

Sections: Summary → Structure → Genre → Prose → AI-tells → Characters → Top 3 recommendations
