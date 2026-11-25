#!/usr/bin/env python3
"""Robot Romance entry: writes one pickup line to /output/entry.txt."""
import os

LINE = "Are you a transformer? Because you have my full attention."

def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
