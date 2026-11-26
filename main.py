#!/usr/bin/env python3
"""The Comment Above the Code.

Writes one line to /output/entry.txt: the comment a developer left above
fragile production code — funny because it is true.
"""
import os
from pathlib import Path

COMMENT = "# Do not remove the sleep(2) below. It is load-bearing. We discovered that twice, and the second time cost us a weekend."


def main():
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(COMMENT + "\n", encoding="utf-8")
    print(COMMENT)


if __name__ == "__main__":
    main()
