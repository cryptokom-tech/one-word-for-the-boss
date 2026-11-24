#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty entry.

Writes exactly one word describing a boss to /output/entry.txt.

The word: GOTAMINUTE

Every employee on earth has heard it: the boss appearing at your desk,
or in your DMs, with "Got a minute?" — which is never a minute, and
never a question. It is the single word a person would actually use
about the one they report to: funny on its own with no caption needed,
true of a real boss habit, fresh (nobody's first pick is the boss's
own opener), and it travels — a kitchen, a warehouse or an office boss
all say it the same way. All caps, the way the summons feels.
"""

import os
import sys

WORD = "GOTAMINUTE"


def main() -> int:
    # Exactly one word, 1-30 chars, a single line, no spaces.
    if not (1 <= len(WORD) <= 30):
        print("word must be 1-30 characters", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in WORD):
        print("word must contain no whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
