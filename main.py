#!/usr/bin/env python3
"""The Absurd Clause Contest -- u-donrulezz-the-absurd-clause-contest-035cc0f1.

Writes one absurd terms-of-service clause (a single line, 1-200 chars)
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, so the
entry can be verified in a private directory).

Python 3.13 standard library only; no network at run time.
"""

import os
from pathlib import Path

ENTRY = "Section 12.3: you grant us a non-exclusive license to your left sock, in perpetuity, worldwide."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
