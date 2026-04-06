# claude-book-plugin

A Claude Code plugin for writing books of any genre — fiction and nonfiction.

**Two modes:** write original prose from scratch, or adapt screenplay/script scenes into narrative prose.

---

## Features

- **20 slash commands** — from project setup to DOCX export
- **18 specialized agents** — 7 core agents + 10 specialized checkers + 1 planner
- **`/full-check`** — complete 10-agent manuscript audit with prioritized dashboard
- **Automatic hooks** — AI writing tell detection after every chapter write; session log on stop
- **Genre craft library** — structural contracts, voice notes, reference books for 10+ genres
- **AI-pattern prevention** — canonical list of AI writing tells, checked at every step
- **DOCX export** — properly formatted manuscript output

---

## Quick start

```bash
# In your book project directory:
/startproject
```

Follow the prompts. Then:

```bash
/outline          # Build chapter plan from your synopsis
/new-chapter 01   # Start writing (from-scratch mode)
/convert 01       # Convert scene (adapt mode)
```

---

## Commands

| Command | Description |
|---------|-------------|
| `/startproject [file]` | Initialize project. Asks mode, genre, POV. Optionally reads a draft. |
| `/new-chapter NN Title` | Write chapter from plan |
| `/convert NN` | Convert screenplay scene to prose |
| `/outline` | Build chapter-by-chapter plan |
| `/rewrite NN notes` | Rewrite chapter with notes |
| `/analyze [NN]` | Full manuscript analysis or single chapter |
| `/full-check [NN\|NN-MM]` | Complete 10-agent audit with dashboard |
| `/check [type]` | Targeted check: continuity-checker / ooc-checker / prose-checker / etc. |
| `/state NN` | Update world state after chapter |
| `/character-sheet Name` | Generate character card |
| `/continuity [range]` | Find continuity errors |
| `/research topic` | Web research with sensory detail |
| `/genre-compass genre — logline` | Generate genre contracts |
| `/style [param value]` | Show or update prose parameters |
| `/stats` | Word count, reading time, chapter breakdown |
| `/compile` | Export to DOCX |
| `/split [file]` | Split large text into chapters |
| `/renumber` | Renumber chapters sequentially |
| `/delete-chapter NN` | Delete chapter and renumber |
| `/type-check` | Diagnostic — mode, genre, setup status |

---

## Agents

### Core agents

| Agent | Description |
|-------|-------------|
| `prose-doctor` | Full manuscript audit |
| `style-validator` | POV, tense, voice consistency |
| `continuity-reviewer` | Timeline, geography, knowledge errors |
| `character-checker` | Voice and behavior consistency |
| `structure-reviewer` | Pacing, acts, arcs, open threads |
| `character-bible` | Extract character list from chapters |
| `story-planner` | Next 3–5 chapter plan based on current progress |

### Specialized checkers (used by `/full-check` and `/check`)

| # | Agent | What it checks |
|----|-------|---------------|
| 1 | `continuity-checker` | Plot and character continuity across chapters |
| 2 | `timeline-checker` | Chronological consistency, travel times, time arithmetic |
| 3 | `consistency-checker` | World rules, setting facts, internal contradictions |
| 4 | `ooc-checker` | Out-of-character behavior, speech pattern violations |
| 5 | `voice-checker` | Narrative voice, POV adherence, character voice distinction |
| 6 | `outline-checker` | Adherence to story/plan.md structure |
| 7 | `pacing-checker` | Scene type balance (action/emotion/world-building) |
| 8 | `prose-checker` | Line-level craft: pacing, show vs tell, dialogue subtext |
| 9 | `high-point-checker` | Satisfaction moment density and quality |
| 10 | `reader-pull-checker` | Chapter hooks, micro-payoffs, reading momentum |

---

## `/full-check` — Complete manuscript audit

Runs all 10 specialized checkers in dependency order:

```
Phase 1 — Foundation:  continuity + timeline + consistency
Phase 2 — Characters:  ooc + voice
Phase 3 — Structure:   outline + pacing
Phase 4 — Reader:      prose + high-point + reader-pull
Phase 5 — Synthesis:   consolidated dashboard
```

Output: `analytics/full-check-dashboard.md` + 10 individual reports

Use for: milestone reviews, before major revision, before submitting.

---

## Project structure

After `/startproject`, your book project will have:

```
my-book/
├── CLAUDE.md              ← mode, genre, POV, style rules
├── chapters/              ← written chapters
├── source/                ← [adapt] screenplay scenes
├── bible/
│   ├── characters/        ← character cards
│   └── universe/          ← locations, world rules
├── story/
│   ├── synopsis.md
│   └── plan.md
├── timeline/events.md
├── state/current/
│   ├── situation.md
│   └── characters.md
├── analytics/             ← full-check reports, research
└── versions/              ← compiled DOCX files
```

---

## Requirements

- Claude Code with plugin support
- Python 3.8+ (hooks + DOCX converter)
- `pip install python-docx` (for `/compile`)

---

## Genre support

**Fiction:** literary, thriller, mystery, romance, fantasy, sci-fi, horror, historical, young-adult, short-story

**Nonfiction:** memoir, narrative-nonfiction, essay, biography, self-help, reportage

Add a new genre by creating `craft/fiction/[genre].md` or `craft/nonfiction/[genre].md`.

---

## License

MIT
