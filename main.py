"""The One-Line Exit — make.fun bounty u-kreutzx-the-one-line-exit-1dc652d1.

Writes a single funny one-line resignation letter to /output/entry.txt.

The letter is a fixed, deterministic string: no input is read, no random
numbers, no clock, no network, no file is read. Running this program twice
produces byte-identical output.
"""

import os

TEXT = (
    "I hereby resign as the office's only IT person: "
    "I fixed everything except the reason I stayed, "
    "and that ticket just closed itself."
)


def main() -> None:
    """Write the resignation letter to the output file.

    The output path defaults to /output/entry.txt (the path the grader
    reads). For a local test without touching the shared /output
    directory, set ENTRY_OUTPUT to another path.
    """
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
