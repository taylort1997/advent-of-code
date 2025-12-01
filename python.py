#!/usr/bin/env python3

import sys
from pathlib import Path

def solve(input_data: str) -> int:
    """
    Solve the puzzle.

    Args:
        input_data: Raw input string

    Returns:
        Solution (change return type as needed)
    """
    lines = input_data.strip().splitlines()
    return len(lines)  # TODO: Implement actual logic

def main():
    """Read input and solve"""
    # Read from input.txt in the same directory as this script
    input_path = Path(__file__).parent / "input.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = sys.stdin.read()

    print(solve(input_data))

if __name__ == "__main__":
    main()
