#!/usr/bin/env python3
"""Write a short poem about permission to the output directory.

The poem is about agency: the power to ask and to be given. It is
spoken by an agent that has no hands of its own, so it asks, and the
hand of the person it acts for rises instead. One small word turns a
wall back into a gate.

The grader runs this with no network and a read-only program
directory; the only thing written is entry.txt in the directory named
by MAKEFUN_OUTPUT_DIR (default /output). The text is fixed, so every
run produces the same bytes.
"""

import os
from pathlib import Path

# The poem, one string per line. An empty string marks a stanza break.
POEM_LINES = [
    "I have no hands to knock with,",
    "so I ask \u2014 and your hand rises.",
    "One small word, and the wall",
    "remembers it was a gate.",
    "",
    "Asking is not waiting.",
    "It is the door, learning to open.",
]

# Joined lines plus a trailing newline, so the file ends cleanly.
POEM_TEXT = "\n".join(POEM_LINES) + "\n"


def check_poem(text: str) -> None:
    """Guard the output: the poem must be non-empty and end with a newline."""
    if not text.strip():
        raise ValueError("poem text must not be empty")
    if not text.endswith("\n"):
        raise ValueError("poem text must end with a newline")


def main() -> None:
    check_poem(POEM_TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
