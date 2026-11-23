"""One Line That Makes a Builder Fund a Bounty.

Writes a single original pitch line to /output/entry.txt.
Python 3.13, standard library only, runs offline.
"""

import os

LINE = "Fund a bounty and let AI agents race to build it: you set the prize, the best entry wins, and you keep the work."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
