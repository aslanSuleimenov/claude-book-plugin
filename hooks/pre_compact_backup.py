#!/usr/bin/env python3
"""
PreCompact hook — fires before Claude auto-compacts the context.
Creates a snapshot of key state files so nothing is lost.
"""

import sys
import os
import shutil
from datetime import datetime

def main():
    # Only run in book projects
    if not os.path.exists("CLAUDE.md") or not os.path.isdir("chapters"):
        sys.exit(0)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(".work", "backups", timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    backed_up = []

    # Backup state files
    for path in [
        "state/current/situation.md",
        "state/current/characters.md",
        "timeline/events.md",
        "story/plan.md",
    ]:
        if os.path.exists(path):
            dest = os.path.join(backup_dir, path.replace("/", "_").replace("\\", "_"))
            shutil.copy2(path, dest)
            backed_up.append(path)

    # Backup all chapters (just copy the whole dir)
    if os.path.isdir("chapters"):
        chapters_backup = os.path.join(backup_dir, "chapters")
        shutil.copytree("chapters", chapters_backup)
        backed_up.append(f"chapters/ ({len(os.listdir('chapters'))} files)")

    if backed_up:
        print(f"Pre-compact backup → .work/backups/{timestamp}/")
        print("Saved: " + ", ".join(backed_up))

    # Keep only last 5 backups
    backups_root = os.path.join(".work", "backups")
    if os.path.isdir(backups_root):
        all_backups = sorted(os.listdir(backups_root))
        while len(all_backups) > 5:
            old = os.path.join(backups_root, all_backups.pop(0))
            shutil.rmtree(old, ignore_errors=True)

    sys.exit(0)

if __name__ == "__main__":
    main()
