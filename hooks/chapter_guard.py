#!/usr/bin/env python3
"""
PostToolUse hook — fires after every Edit or Write.
If the file is in chapters/, check for forbidden patterns and AI writing tells.
Prints warnings to stderr (visible to Claude as hook feedback).
"""

import sys
import os
import json
import re

def get_tool_input():
    """Read tool input from stdin (Claude passes it as JSON)."""
    try:
        data = json.load(sys.stdin)
        return data
    except Exception:
        return {}

def is_chapter_file(file_path: str) -> bool:
    """Check if the file is in a chapters/ directory."""
    normalized = file_path.replace("\\", "/")
    return "/chapters/" in normalized or normalized.startswith("chapters/")

def check_patterns(content: str) -> list[str]:
    """Check for forbidden AI writing tells. Returns list of warning messages."""
    warnings = []

    # Rule of three — three-item lists in descriptions
    three_pattern = re.compile(r'\b\w+[,;]\s+\w+[,;]\s+and\s+\w+', re.IGNORECASE)
    matches = three_pattern.findall(content)
    if len(matches) > 2:
        warnings.append(f"RULE OF THREE: {len(matches)} instances found. Vary list structures.")

    # Emotional placeholders
    emotional_placeholders = [
        r'\bshe felt\b', r'\bhe felt\b', r'\bthey felt\b',
        r'\bshe was overwhelmed\b', r'\bhe was overwhelmed\b',
        r'\bshe was devastated\b', r'\bhe was devastated\b',
        r'\bshe realized\b', r'\bhe realized\b',
        r'\bshe knew\b(?! that)', r'\bhe knew\b(?! that)',
        r'\bshe understood\b', r'\bhe understood\b',
        r'\bemotion[s]?\b.*\bwash\b', r'\bwave of\b.*\bwash\b',
    ]
    for pattern in emotional_placeholders:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            warnings.append(f"EMOTIONAL PLACEHOLDER: '{matches[0]}' — use concrete image instead.")

    # Dialogue explaining feelings (speaker explains own emotion)
    dialogue_tells = [
        r'"[^"]*I\'m so (angry|sad|happy|scared|nervous|excited)[^"]*"',
        r'"[^"]*I feel (angry|sad|happy|scared|nervous|excited)[^"]*"',
        r'"[^"]*because I (love|hate|fear|need)[^"]*"',
    ]
    for pattern in dialogue_tells:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            warnings.append(f"DIALOGUE EXPLAINS FEELING: '{matches[0][:60]}...' — let subtext carry it.")

    # Sudden/suddenly overuse
    suddenly_count = len(re.findall(r'\bsuddenly\b', content, re.IGNORECASE))
    if suddenly_count > 2:
        warnings.append(f"SUDDENLY: used {suddenly_count} times. Vary transitions.")

    # Nodding/smiling/sighing — common AI filler gestures
    filler_gestures = re.findall(r'\b(nodded|smiled|sighed|shrugged)\b', content, re.IGNORECASE)
    if len(filler_gestures) > 4:
        warnings.append(f"FILLER GESTURES: {len(filler_gestures)} instances of nod/smile/sigh/shrug. Vary character physicality.")

    # Abstract state over concrete image
    abstract_states = [
        r'\bthe air was thick with tension\b',
        r'\bsilence stretched\b',
        r'\btime seemed to slow\b',
        r'\bthe world seemed\b',
        r'\bsomething in (?:her|his|their) eyes\b',
    ]
    for pattern in abstract_states:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(f"ABSTRACT CLICHÉ: '{pattern}' — replace with specific concrete detail.")

    return warnings

def main():
    data = get_tool_input()

    # Get the file path from tool input
    file_path = data.get("tool_input", {}).get("file_path", "")
    if not file_path:
        # Try alternate key
        file_path = data.get("file_path", "")

    if not file_path or not is_chapter_file(file_path):
        sys.exit(0)  # Not a chapter file — nothing to do

    # Read the file content
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"chapter_guard: could not read {file_path}: {e}", file=sys.stderr)
        sys.exit(0)

    warnings = check_patterns(content)

    if warnings:
        print("\n⚠️  chapter_guard warnings:", file=sys.stderr)
        for w in warnings:
            print(f"  • {w}", file=sys.stderr)
        print("  Review against: ${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md\n", file=sys.stderr)

    sys.exit(0)

if __name__ == "__main__":
    main()
