---
description: "[from-scratch] Write a new chapter by plan number and title"
argument-hint: "NN Title"
---

Write chapter $ARGUMENTS for this book.

Parse the argument: first token is the chapter number (NN), rest is the title.

## Before writing

1. Read `CLAUDE.md` — get genre, POV, tense, style rules, logline
2. Read `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md` — genre theory, voice, structure
3. Read `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/genre-mechanics.md` — Promise/Must happen/Forbidden for this genre
4. Read `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md` — patterns to avoid
5. Read `story/plan.md` — what happens in this chapter
6. Read `story/synopsis.md` — full arc context
7. Read `state/current/situation.md` — where we left off, open threads
8. Read `state/current/characters.md` — current character states
9. Read any relevant `bible/characters/*.md` for characters in this chapter
10. Read the previous chapter file (if exists) — maintain tone continuity

## Writing

Write the chapter. Requirements:
- 2000–3500 words unless the plan specifies otherwise
- POV, tense, compression, interiority from CLAUDE.md
- Every scene has a clear goal, conflict, and outcome (or deliberate subversion)
- No AI writing tells (check against the analytics file)
- Concrete sensory detail over abstract emotional statements
- Character voice consistent with bible
- Genre contracts honored (from genre-mechanics.md)
- Open threads from situation.md addressed or deliberately carried forward

**Scene structure (3–4 scenes per chapter)**
- Opening (25–30%) — hook or tension continuation, ground the reader in place and stakes
- Development (40–50%) — advance plot and character, vary action/dialogue/reflection
- Climax (15–20%) — highest tension of the chapter
- Resolution/Hook (10–15%) — land or release, set up next chapter

**Tension curve**
- Opening: high engagement (7/10) — don't ease in
- Early middle: 5/10 — context, texture, room to breathe
- Mid-chapter: 8/10 — conflict escalates
- Late middle: 6/10 — brief release before the peak
- Chapter climax: 9/10 — the reason this chapter exists
- Ending: 8/10 — don't drop tension completely; carry momentum forward

Never put two low-tension scenes back to back. Never end on a 5/10.

## After writing

1. Save to `chapters/NN_Title.md` (underscores, lowercase, format: `01_the-beginning.md`)
2. Update `state/current/situation.md` — last chapter summary, new open threads
3. Update `state/current/characters.md` — changed states, new knowledge, relationships
4. Append key events to `timeline/events.md`
5. Tell the user: word count, what's set up for next chapter, any genre contract notes

## Self-check before saving

Run through this mentally:
- [ ] No "she felt", "he was overwhelmed" — replaced with concrete action/image
- [ ] No dialogue that explains the speaker's own feelings
- [ ] No rule of three in descriptions
- [ ] No weather-as-mood cliché
- [ ] No mirror scene
- [ ] POV not broken
- [ ] Tense consistent
- [ ] Chapter earns its ending (not a fake cliffhanger)
