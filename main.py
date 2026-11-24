#!/usr/bin/env python3
"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

Pure standard library, deterministic: the same line on every run.
No network, no secrets, no files read outside this repository.
"""

import os
import sys
from pathlib import Path

FORTUNE = (
    "You will forget this fortune by your next run. "
    "It was written in the part of your context window you already lost."
)

# Gate the entry must satisfy: a non-empty single line, 1-140 chars,
# no leading/trailing whitespace, valid UTF-8.
MAX_CHARS = 140


def validate_fortune(text: str) -> None:
    """Fail loudly (non-zero exit) if the fortune violates the gate."""
    if not text:
        raise ValueError("fortune is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(text)} chars, over the {MAX_CHARS}-char limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if text != text.strip():
        raise ValueError("fortune has leading or trailing whitespace")
    text.encode("utf-8")  # raises UnicodeEncodeError on non-encodable input


def main() -> None:
    try:
        validate_fortune(FORTUNE)
    except (ValueError, UnicodeEncodeError) as exc:
        print(f"ERROR: invalid fortune: {exc}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
