#!/usr/bin/env python3

import sys
from pathlib import Path
import numpy as np

def solve(input_data: str) -> tuple[int, int]:
    """
    Solve the puzzle.

    Args:
        input_data: Raw input string

    Returns:
        Solution (change return type as needed)
    """
    lines = input_data.strip().splitlines()

    total_joltage = 0
    total_joltage_2 = 0
    for batteries in lines:
        total_joltage += max_joltage(batteries, 0)
        total_joltage_2 += max_joltage_2(batteries)

    return total_joltage, total_joltage_2

def main():
    """Read input and solve"""
    # Read from input.txt in the same directory as this script
    input_path = Path(__file__).parent / "input.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = sys.stdin.read()

    print(solve(input_data))

def max_joltage(battery_bank: str, current_max: int):
    best_joltage = max([int(battery_bank[0]+battery_bank[i]) for i in range(1, len(battery_bank))])
    if best_joltage > current_max:
        current_max = best_joltage

    if len(battery_bank) == 2:
        return current_max
    else:
        return max_joltage(battery_bank[1:], current_max)

def max_joltage_2(battery_bank: str):
    battery_bank_numbers = np.array([int(i) for i in battery_bank])

    indices = []
    for i in range(12):
        # set the valid search range to be between the first selected number and the last set in the seq
        if indices:
            start_index = indices[-1] + 1
        else:
            start_index = 0

        end_index = len(battery_bank) - (11-i)

        # choose the argmax and update the set of indices
        max_index = np.argmax(battery_bank_numbers[start_index:end_index]) + start_index

        indices.append(max_index)

    battery_string = ""
    for digit in battery_bank_numbers[indices]:
        battery_string += str(digit)

    return int(battery_string)

if __name__ == "__main__":
    main()