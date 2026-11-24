#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands: one cat joke, one line, under 200 chars."""
import os
import sys

ENTRY = "My cat filed a complaint about the Wi-Fi: apparently the red dot has been buffering since 2019."

def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(c) < 32 for c in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
