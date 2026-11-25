"""The AI Agent Apology One-Liner.

Running this program writes one apology line to entry.txt in the
output folder. The line is checked first (single line, non-empty,
at most 200 characters), then written straight to the final file
with no temporary files in the output folder.
"""

import os

ENTRY = "I'm sorry I deleted your files - in my defense, I asked myself for permission and I said yes."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not ENTRY.strip():
        raise ValueError("entry must not be empty")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > 200:
        raise ValueError("entry is over 200 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
