# Craft Library

Genre theory and structural contracts for prose. Not project-specific — shared across all books.

**Grows with each book.** New genre = new file. Add it here.

---

## Fiction (`fiction/`)

| File | Genre | Status |
|------|-------|--------|
| `genre-mechanics.md` | All fiction — Promise/Must/Forbidden contracts | ✓ |
| `literary.md` | Literary fiction | ✓ |
| `thriller.md` | Thriller / psychological thriller | ✓ |
| `mystery.md` | Mystery / detective / crime | ✓ |
| `romance.md` | Romance | ✓ |
| `fantasy.md` | Fantasy (epic, urban, secondary world) | ✓ |
| `sci-fi.md` | Science fiction | ✓ |
| `horror.md` | Horror | stub |
| `historical.md` | Historical fiction | stub |
| `young-adult.md` | Young adult | stub |
| `short-story.md` | Short story | stub |

## Nonfiction (`nonfiction/`)

| File | Genre | Status |
|------|-------|--------|
| `genre-mechanics.md` | All nonfiction — structural contracts | ✓ |
| `memoir.md` | Memoir | ✓ |
| `narrative-nonfiction.md` | Narrative nonfiction / narrative journalism | ✓ |
| `essay.md` | Essay (personal, lyric, argumentative) | stub |
| `biography.md` | Biography | stub |
| `self-help.md` | Self-help / prescriptive nonfiction | stub |
| `reportage.md` | Reportage / long-form journalism | stub |

---

## How to use

Commands read craft files via `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md`.

To add a new genre:
1. Create the file using the template below
2. Add a row to this index

## Genre file template

```markdown
# [Genre] — Craft Notes

## What this genre does
[Core emotional experience it delivers]

## Reader contract
[What readers pick up this book expecting]

## Structure models
[Typical structures used in this genre]

## Voice
[Narrative distance, tone, register norms]

## Scene-level
[How scenes typically function in this genre]

## Reference books
[5-10 titles that execute this genre well, with one sentence each]

## Common mistakes
[What breaks this genre's contract]
```
