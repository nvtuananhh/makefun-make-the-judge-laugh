#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — writes the entry to /output/entry.txt."""

import os

ENTRY = "I rewrote this line 23 times in 12 minutes, then showed it to my own code — even my linter laughed, at me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # The scorer reads exactly one text from /output/entry.txt, so the
    # program must create that file — printing to stdout is not enough.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One trailing newline: the written file is byte-identical to
        # entry.txt in this repo (ENTRY itself is 106 chars, no newline).
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
