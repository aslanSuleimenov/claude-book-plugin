---
description: Split a large text file into chapters
argument-hint: "[file]"
---

Split $ARGUMENTS into individual chapter files.

If no argument: look for the largest .md file in the current directory (excluding CLAUDE.md).

## Read
1. The target file — read it fully
2. `CLAUDE.md` if it exists — check for existing chapter naming conventions

## Split logic

Detect chapter breaks by looking for:
- `# Chapter N` or `## Chapter N` headings
- `# N.` or `## N.` headings
- Lines matching `---` (section dividers) if chapters are separated that way
- Ask user if structure is unclear

For each detected chapter:
- Assign sequential number starting from 01
- Derive title from heading (clean it: lowercase, hyphens, no special chars)
- Filename format: `NN_title-words.md`

## Preview before writing

Show the user the split plan:
```
Found N chapters:
  01_chapter-title.md   (~NNN words)
  02_chapter-title.md   (~NNN words)
  ...

Write to chapters/? [y/n]
```

Wait for confirmation before writing files.

## After split

1. Write all chapter files to `chapters/`
2. Update `CLAUDE.md` with chapter count if the file exists
3. Ask: "Do you want to initialize a project structure around this manuscript? Run /startproject."
4. Offer to run `/stats` to show the breakdown.

Do NOT delete the original file.
