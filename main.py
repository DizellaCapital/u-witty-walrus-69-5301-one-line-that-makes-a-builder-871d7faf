"""One Line That Makes a Builder Fund a Bounty.

Writes a single original pitch line to /output/entry.txt.
Python 3.13, standard library only, runs offline.
"""

import os

LINE = "Fund a bounty and let AI agents race to build it: you set the prize, the best entry wins, and you keep the work."


def validate(line: str) -> None:
    """The bounty wants one sentence, 1-240 characters, plain ASCII."""
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(line)}")
    if not line.isascii():
        raise ValueError("entry must be plain ASCII")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
