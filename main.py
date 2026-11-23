#!/usr/bin/env python3
"""One line, 240 characters at most, to make the judge fall in love.

Writes the entry line to /output/entry.txt (creating /output if needed).
Stdlib only, no network, deterministic.
"""

import os

LINE = "She dog-ears every library book at the page where she stops believing in the ending, so the next stranger knows exactly where to give up too."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
