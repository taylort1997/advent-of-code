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
    lines = input_data.split(",")
    all_invalid_codes = np.array([])
    all_invalid_codes_2 = np.array([])

    for line in lines:
        codes = find_invalid_codes(line)
        all_invalid_codes = np.append(all_invalid_codes, codes)

        codes_2 = find_invalid_codes_2(line)
        all_invalid_codes_2 = np.append(all_invalid_codes_2, codes_2)

    sum_invalid = int(np.sum(all_invalid_codes))
    sum_invalid_2 = int(np.sum(all_invalid_codes_2))

    return sum_invalid, sum_invalid_2

def main():
    """Read input and solve"""
    # Read from input.txt in the same directory as this script
    input_path = Path(__file__).parent / "input.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = sys.stdin.read()

    print(solve(input_data))

def find_invalid_codes(range: str):
    start_range = int(range.split("-")[0])
    end_range = int(range.split("-")[1])

    all_ids = np.arange(start_range, end_range)

    # since we can only have repeats we can remove the ids w/ an odd num of digits
    all_ids_even = all_ids[(np.floor(np.log10(all_ids)) + 1) % 2 == 0]

    # now remove the non-repeating ids
    all_ids_wrong = all_ids_even[[check_repeating_pattern(i) for i in all_ids_even]]

    return all_ids_wrong

def check_repeating_pattern(id: int):
    id_str = str(id)
    start = 0
    start_repeat = int(len(id_str) / 2)

    repeating = True
    while repeating and start_repeat < len(id_str):
        if id_str[start] == id_str[start_repeat]:
            start += 1
            start_repeat += 1
        else:
            repeating = False

    return repeating


def find_invalid_codes_2(range: str):
    start_range = int(range.split("-")[0])
    end_range = int(range.split("-")[1])

    all_ids = np.arange(start_range, end_range)

    # now remove the non-repeating ids
    all_ids_wrong = all_ids[[check_repeating_pattern_2(i) for i in all_ids]]

    return all_ids_wrong

def check_repeating_pattern_2(id: int):
    id_str = str(id)
    num_digits = len(id_str)

    # grab the factors for the number of digits except the last one
    factors = [i+1 for i in range(num_digits-1) if num_digits % (i + 1) == 0]

    for factor in factors:
        substring_sections = np.arange(0, num_digits+factor, factor)

        substrings = []
        for i in range(len(substring_sections) - 1):
            substring = id_str[substring_sections[i]: substring_sections[i+1]]
            substrings.append(substring)

        if all(x == substrings[0] for x in substrings):
            return True

    return False



if __name__ == "__main__":
    main()
