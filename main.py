"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt), with no trailing newline. Python 3.13, standard
library only, deterministic, no network.
"""

import os

JOKE = (
    "I sent a company-wide email begging people to stop replying all "
    "\u2014 300 people replied all to say they agree."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
