# claude-book-plugin — Start Here

## Installation

1. Clone or copy this plugin into your Claude Code plugins directory
2. Add to your `settings.json`:
   ```json
   {
     "plugins": ["path/to/claude-book-plugin"]
   }
   ```
3. Restart Claude Code

## Starting a new book

1. Create a new empty folder for your book
2. Open it in Claude Code
3. Run:
   ```
   /startproject
   ```
   Claude will ask you for mode, genre, POV, and a logline. It creates all the project structure.

4. Fill in `story/synopsis.md` (your full story from beginning to end)
5. Run `/outline` to build a chapter plan
6. Run `/new-chapter 01 Opening` (from-scratch) or `/convert 01` (adapt) to start writing

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
| `/check` | Full quality check (style, continuity, characters, structure) |
| `/analyze` | Deep manuscript analysis |
| `/state NN` | Update world state after chapter |
| `/stats` | Word count, reading time, chapter breakdown |
| `/compile` | Export to DOCX |
| `/type-check` | Diagnose project setup |

## Agents (invoke in conversation)

- `prose-doctor` — full manuscript audit
- `style-validator` — POV/tense/voice consistency
- `continuity-reviewer` — timeline, geography, knowledge errors
- `character-checker` — voice and behavior consistency
- `structure-reviewer` — pacing, acts, arcs, open threads
- `character-bible` — extract full character list from chapters

## Requirements

- Claude Code with plugin support
- Python 3.8+ (for hooks and DOCX converter)
- `pip install python-docx` (for `/compile`)
