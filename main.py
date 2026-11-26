"""Write one developer comment to the entry file.

The program produces a single line: the kind of comment a developer
leaves above fragile production code, funny precisely because it is
true. The line is emitted verbatim to entry.txt.
"""

import os

COMMENT = (
    "# DO NOT remove this sleep. We took it out once and the whole system "
    "fell over. Nobody knows why, and nobody is brave enough to ask."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(COMMENT + "\n")


if __name__ == "__main__":
    main()
