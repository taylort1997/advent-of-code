#!/usr/bin/env python3

import sys
from pathlib import Path

def solve(input_data: str) -> tuple[int, int]:
    """
    Solve the puzzle.

    Args:
        input_data: Raw input string

    Returns:
        Solution (change return type as needed)
    """
    lines = input_data.strip().splitlines()

    current_value = 50
    times_past_zero = 0
    times_at_zero = 0

    for line in lines:
        direction = line[0]
        size = int(line[1:])

        if direction == "L":
            new_value = current_value - size
        else:
            new_value = current_value + size

        times_past_zero += abs(new_value // 100)
        times_at_zero += 1 if new_value % 100 == 0 else 0

        current_value = new_value % 100

    return times_at_zero, times_past_zero


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
