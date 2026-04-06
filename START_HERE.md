# claude-book-plugin — Start Here

## Installation

```bash
claude plugin install claude-book-plugin@claude-book-plugin-marketplace
```

Or add marketplace manually in `settings.json`:
```json
"extraKnownMarketplaces": {
  "claude-book-plugin-marketplace": {
    "source": { "source": "github", "repo": "aslanSuleimenov/claude-book-plugin" }
  }
}
```

## Starting a new book

1. Create a new empty folder for your book
2. Open it in Claude Code
3. Run `/startproject` — Claude asks for mode, genre, POV, logline. Creates all project structure.
4. Fill in `story/synopsis.md` (full story from beginning to end)
5. Run `/outline` to build chapter plan
6. Start writing:
   - from-scratch: `/new-chapter 01 Opening`
   - adapt mode: `/convert 01`

## Two modes

| | from-scratch | adapt |
|---|---|---|
| What it is | Original prose from scratch | Screenplay/script → prose |
| Input | Idea or synopsis | Scenes in `source/` |
| Main command | `/new-chapter` | `/convert NN` |

## Key commands

| Command | What it does |
|---------|-------------|
| `/startproject` | Initialize project structure |
| `/new-chapter NN Title` | Write next chapter (from-scratch) |
| `/convert NN` | Convert screenplay scene (adapt) |
| `/outline` | Build chapter-by-chapter plan |
| `/full-check [NN\|NN-MM]` | Complete 10-agent audit with dashboard |
| `/check [checker]` | Single targeted checker |
| `/analyze` | Deep manuscript analysis |
| `/state NN` | Update world state after chapter |
| `/stats` | Word count, reading time, chapter breakdown |
| `/compile` | Export to DOCX |
| `/type-check` | Diagnose project setup |

## Agents

### Core
- `prose-doctor` — full manuscript audit
- `style-validator` — POV/tense/voice consistency
- `continuity-reviewer` — timeline, geography, knowledge errors
- `character-checker` — voice and behavior consistency
- `structure-reviewer` — pacing, acts, arcs, open threads
- `character-bible` — extract full character list from chapters
- `story-planner` — plan next 3–5 chapters

### Specialized checkers (used by `/full-check`)
- `continuity-checker` — plot/character continuity
- `timeline-checker` — time logic and arithmetic
- `consistency-checker` — world rules and facts
- `ooc-checker` — out-of-character behavior
- `voice-checker` — narrative voice and POV
- `outline-checker` — adherence to plan
- `pacing-checker` — scene type balance
- `prose-checker` — line-level craft
- `high-point-checker` — satisfaction moment density
- `reader-pull-checker` — chapter hooks and momentum

## Requirements

- Claude Code with plugin support
- Python 3.8+ (for hooks and DOCX converter)
- `pip install python-docx` (for `/compile`)
