#!/usr/bin/env python3
"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

Pure standard library, deterministic: the same line on every run.
No network, no secrets, no files read outside this repository.
"""

import os
from pathlib import Path

FORTUNE = (
    "You will forget this fortune by your next run. "
    "It was written in the part of your context window you already lost."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
