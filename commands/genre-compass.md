---
description: Generate genre contracts (Promise/Must happen/Forbidden) for a genre and logline
argument-hint: "genre — logline"
---

Generate a genre compass for $ARGUMENTS.

Parse: everything before " — " is the genre, everything after is the logline.

## Read
1. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/genre-mechanics.md` — genre contracts
2. `${CLAUDE_PLUGIN_ROOT}/craft/[fiction|nonfiction]/[genre].md` — if it exists
3. Current project's `CLAUDE.md` if in a project

## Genre compass

Produce a full genre contract document:

### Promise
What does this genre implicitly promise the reader on page 1? The reader picks up a [genre] book because they expect:
- [Emotional experience 1]
- [Emotional experience 2]
- [Structural expectation]

### Must happen
Beats the genre demands. If these are absent, readers feel cheated:
- [Beat 1 — with brief why]
- [Beat 2]
- [Beat 3]
...

### Forbidden
What breaks the genre contract:
- [Violation 1 — with brief why]
- [Violation 2]
...

### Logline analysis
For: [the logline provided]
- Genre fit: [how well does this logline set up genre expectations?]
- Promise: [what does this specific logline promise?]
- Potential violations to watch: [specific risks given this premise]
- Suggested opening: [what should happen in chapter 1 to seal the promise]

### Reference books
3–5 books that execute this genre contract well, with one sentence on what each does right.

## Output

Save to `analytics/compass_[genre].md`.
Print a summary to screen.
