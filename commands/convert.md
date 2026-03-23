---
description: "[adapt] Convert a screenplay scene from source/ into prose"
argument-hint: "NN"
---

Convert source scene $ARGUMENTS from screenplay to narrative prose.

## Before converting

1. Read `CLAUDE.md` — get POV, tense, compression, interiority, style rules
2. Read `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md`
3. Read `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`
4. Find and read `source/NN*.md` (or `source/NN*.fountain`, `.fdx`, `.txt`)
5. Read `state/current/situation.md` and `state/current/characters.md`
6. Read relevant `bible/characters/*.md`

## Conversion parameters

From CLAUDE.md:
- **compression**: `minimal` (close to scene length) / `moderate` (×1.5–2) / `expansive` (×2.5–4)
- **interiority**: `low` (mostly external) / `medium` (some POV thoughts) / `high` (deep inner life)

## Conversion rules

**What screenplay gives you:** action lines (what camera sees), dialogue, scene headings
**What prose needs:** interiority, sensory texture, subtext in dialogue, time/space handling, rhythm

Translate:
- Action lines → prose with sensory detail appropriate to interiority level
- Dialogue → keep subtext, remove on-the-nose explanations, adjust to prose rhythm
- Scene headings → temporal/spatial grounding in prose
- Parentheticals → body language, not explicit emotion labels
- Montage sequences → compression or expanded rhythm depending on parameter
- Intercut scenes → handle POV transitions deliberately

Do NOT:
- Translate action lines verbatim
- Keep screenplay formatting or stage directions
- Add emotions that aren't in the scene (interiority ≠ invention)
- Lose the scene's dramatic function

## After converting

1. Save to `chapters/NN_Title.md` — derive title from scene heading or ask user
2. Update `state/current/situation.md` and `state/current/characters.md`
3. Append key events to `timeline/events.md`
4. Report: word count, compression ratio achieved, interiority notes
