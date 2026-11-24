#!/usr/bin/env python3
"""Fortune in a Pot entry (make.fun).

Writes a single original fortune for a houseplant, at most 120
characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when the harness sets it). Stdlib only; no network, no files read,
no secrets.

The line: a prediction for the plant on the windowsill. A sunbeam
is about to single out its newest leaf for the best light, and the
rest of the windowsill will quietly claim the credit. The joke is
the windowsill's petty pride; the fortune stays warm — the plant
is the chosen one, and spring is on its side.
"""

import os
import sys

MAX_CHARS = 120

FORTUNE = (
    "Soon a sunbeam will choose your newest leaf, and the whole "
    "windowsill will quietly take credit for it."
)


def validate(text: str) -> str:
    """Return the stripped line, enforcing the gate's 1-120 char rule."""
    text = text.strip()
    if not text:
        raise ValueError("fortune is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    return text


def write_entry(text: str, out_dir: str) -> str:
    """Write the fortune to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read what was written and confirm it matches, so a partial
    # write or encoding slip is caught here instead of in grading.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError(f"entry.txt mismatch: wrote {len(text)} chars, read back {len(written)}")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = validate(FORTUNE)
    path = write_entry(text, out_dir)
    print(text)
    print(f"wrote {len(text)} chars to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
