"""Entry for make.fun "The Robot Vacuum's Funniest Excuse" (u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = "That spot wasn't missed, it was a union break. My suction filed a complaint and honestly, I side with it."

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
