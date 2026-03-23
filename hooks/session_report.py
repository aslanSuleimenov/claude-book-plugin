#!/usr/bin/env python3
"""
Stop hook — fires at end of session.
Writes a log of modified files to state/session_log.md.
"""

import sys
import os
import json
import subprocess
from datetime import datetime

def get_modified_files() -> list[str]:
    """Get list of modified files using git diff."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, timeout=10
        )
        files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

        # Also check untracked files in chapters/
        result2 = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard", "chapters/"],
            capture_output=True, text=True, timeout=10
        )
        untracked = [f.strip() for f in result2.stdout.strip().split("\n") if f.strip()]
        return files + untracked
    except Exception:
        return []

def get_chapter_stats(file_path: str) -> str:
    """Get word count for a chapter file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        words = len(content.split())
        return f"{words:,} words"
    except Exception:
        return "?"

def main():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")

    modified = get_modified_files()
    if not modified:
        sys.exit(0)  # Nothing changed this session

    # Build report
    chapter_files = [f for f in modified if "chapters/" in f.replace("\\", "/")]
    other_files = [f for f in modified if "chapters/" not in f.replace("\\", "/")]

    lines = [
        f"## Session {date_str} {time_str}\n",
    ]

    if chapter_files:
        lines.append("### Chapters modified")
        for f in chapter_files:
            stats = get_chapter_stats(f)
            lines.append(f"- `{f}` ({stats})")
        lines.append("")

    if other_files:
        lines.append("### Other files modified")
        for f in other_files:
            lines.append(f"- `{f}`")
        lines.append("")

    lines.append("---\n")

    # Ensure state/ directory exists
    os.makedirs("state", exist_ok=True)

    log_path = "state/session_log.md"

    # Prepend to existing log (newest first)
    existing = ""
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            existing = f.read()

    header = "# Session Log\n\n" if not existing.startswith("# Session Log") else ""

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(lines))
        if existing:
            # Remove existing header if present
            existing_body = existing.replace("# Session Log\n\n", "")
            f.write(existing_body)

    sys.exit(0)

if __name__ == "__main__":
    main()
