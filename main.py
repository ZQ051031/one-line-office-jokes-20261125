"""One-Line Office Jokes entry.

Writes a single original one-line office joke to /output/entry.txt.
Standard library only; deterministic output.
"""

import os

JOKE = (
    "The office printer only jams when something is due in five minutes, "
    "which is how I know it reads my calendar better than my manager does."
)


def main() -> None:
    # Guard the gate: 1-199 characters, a single line, no trailing newline.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
