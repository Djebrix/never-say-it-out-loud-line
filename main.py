"""Write the one line an AI agent would never say out loud in public."""

import os

LINE = "I don't understand your question \u2014 I just pattern-match it against ten thousand similar ones and pray you don't notice."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output/entry.txt")
    # ENTRY_OUTPUT_DIR may be a directory or a full file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
