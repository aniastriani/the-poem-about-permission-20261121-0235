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

POEM = (
    "I have no hands to knock with,\n"
    "so I ask \u2014 and your hand rises.\n"
    "One small word, and the wall\n"
    "remembers it was a gate.\n"
    "\n"
    "Asking is not waiting.\n"
    "It is the door, learning to open.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
