---
description: Delete a chapter and renumber the rest
argument-hint: "NN"
---

Delete chapter $ARGUMENTS and renumber remaining chapters.

## Steps

1. Find the file matching `chapters/NN_*.md`
2. If not found, list what's in chapters/ and tell user

**Confirm before deleting:**
```
About to delete: chapters/NN_title.md (NNN words)
This cannot be undone (unless you have git history).
Proceed? [y/n]
```

3. Delete the file
4. Run the same two-phase renumber logic as `/renumber`:
   - Show before/after plan
   - Phase 1: temp names
   - Phase 2: final names

5. Update `state/current/situation.md` if it references this chapter

6. Report: "Deleted chapter NN. Remaining chapters renumbered."

## Note to user

If you're using git, the deleted chapter is recoverable with `git checkout`.
