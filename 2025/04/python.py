#!/usr/bin/env python3

import sys
from pathlib import Path
import numpy as np
import scipy

def solve(input_data: str) -> tuple[int, int]:
    """
    Solve the puzzle.

    Args:
        input_data: Raw input string

    Returns:
        Solution (change return type as needed)
    """
    lines = input_data.strip().splitlines()
    bin_array = input_to_binary_array(lines)

    all_rolls_removed = []
    rolls_array = bin_array
    all_removed = False
    while all_removed == False:
        accessible_rolls = fewer_than_four(rolls_array)
        rolls_removed = int(np.sum(accessible_rolls))
        rolls_array = rolls_array - accessible_rolls
        all_rolls_removed.append(rolls_removed)

        if rolls_removed == 0:
            all_removed = True

    return all_rolls_removed[0], sum(all_rolls_removed)  # TODO: Implement actual logic

def main():
    """Read input and solve"""
    # Read from input.txt in the same directory as this script
    input_path = Path(__file__).parent / "input.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = sys.stdin.read()

    print(solve(input_data))

def input_to_binary_array(lines: list[str]):
    binary_lines = []
    for line in lines:
        binary_line = [1 if i == "@" else 0 for i in list(line)]
        binary_lines.append(binary_line)
    array = np.array(binary_lines)

    return array

def fewer_than_four(array):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    num_neighbours = scipy.signal.convolve2d(array, kernel, boundary="fill", mode="same")
    less_four = num_neighbours < 4
    accessible = np.logical_and(less_four, array)

    return accessible

if __name__ == "__main__":
    main()
