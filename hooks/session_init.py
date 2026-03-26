#!/usr/bin/env python3
"""
SessionStart hook — fires at the beginning of each session.
Prints current project state so Claude loads context immediately.
"""

import sys
import os

def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return ""

def count_words(path: str) -> int:
    content = read_file(path)
    return len(content.split()) if content else 0

def main():
    # Only run if this looks like a book project
    if not os.path.exists("CLAUDE.md"):
        sys.exit(0)

    claude_md = read_file("CLAUDE.md")
    # Simple heuristic: book projects have chapters/ directory
    if not os.path.isdir("chapters"):
        sys.exit(0)

    lines = ["=== Book project context ==="]

    # Chapter count and word total
    chapter_files = sorted([
        f for f in os.listdir("chapters")
        if f.endswith(".md")
    ]) if os.path.isdir("chapters") else []

    if chapter_files:
        total_words = sum(
            count_words(os.path.join("chapters", f))
            for f in chapter_files
        )
        lines.append(f"Chapters: {len(chapter_files)} ({total_words:,} words)")
        lines.append(f"Last chapter: {chapter_files[-1]}")
    else:
        lines.append("Chapters: none yet")

    # Current situation
    situation = read_file("state/current/situation.md")
    if situation:
        # Take first 20 lines
        preview = "\n".join(situation.splitlines()[:20])
        lines.append(f"\n--- state/current/situation.md ---\n{preview}")

    lines.append("=== end context ===")
    print("\n".join(lines))
    sys.exit(0)

if __name__ == "__main__":
    main()
