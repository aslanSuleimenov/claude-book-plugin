---
description: Web research with sensory details, jargon, and primary sources
argument-hint: "topic"
---

Research $ARGUMENTS for use in this book.

## Context
1. Read `CLAUDE.md` — genre, setting, time period
2. Check if there's existing research in `analytics/` on this topic

## Research approach

This is research for creative prose, not an essay. The goal is:
- **Sensory details** — what it smells, sounds, feels, looks like
- **Authentic jargon** — what insiders actually say (not textbook terms)
- **Texture** — details that make a reader feel they're there
- **Edge cases** — the unexpected facts that make fiction feel real
- **Primary sources** — first-person accounts, not just Wikipedia

Search the web for the topic. Prioritize:
- First-person accounts (memoirs, interviews, forums, oral histories)
- Domain-specific sources (professional, technical, community)
- Historical primary sources if period research
- Sensory/experiential descriptions

## Output format

Save to `analytics/research_[topic-slug].md`:

```markdown
# Research: [Topic]
Date: [today]
For: [book title from CLAUDE.md]

## Key facts
[Bulleted facts relevant to the book]

## Sensory details
[Smells, sounds, textures, tastes, sights — specific and unexpected]

## Jargon and authentic language
[Real terms, phrases, speech patterns of people in this world]

## Unexpected / counterintuitive
[Things that surprised you — these make fiction feel real]

## Sources
[List sources with URLs]

## Story notes
[How this could be used: scenes, dialogue, character knowledge]
```

After saving, give the user a 3-sentence summary of the most useful findings.
