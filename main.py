"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt), with no trailing newline. Python 3.13, standard
library only, deterministic, no network.
"""

import os

JOKE = (
    "I emailed the whole company \u2018please stop replying all\u2019 "
    "\u2014 300 people replied all to agree, including HR."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
