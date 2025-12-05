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

    sep_index = lines.index("")
    range_ids = lines[:sep_index]
    check_ids = lines[sep_index+1:]

    lookup = fresh_lookup(range_ids)
    fresh = fresh_check(check_ids, lookup)

    all_fresh = fresh_all(lookup)

    return len(fresh), all_fresh

def main():
    """Read input and solve"""
    # Read from input.txt in the same directory as this script
    input_path = Path(__file__).parent / "input.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = sys.stdin.read()

    print(solve(input_data))

def fresh_lookup(fresh_ranges: list[str]):
    lookup = []
    for id in fresh_ranges:
        split = id.split("-")
        fresh_min = int(split[0])
        fresh_max = int(split[1])
        lookup.append((fresh_min, fresh_max))

    return lookup

def fresh_all(fresh_ranges: list[tuple[int, int]], debug=False):
    fresh_sorted = sorted(fresh_ranges)
    num_fresh = 0
    prev_max = 0
    for i in fresh_sorted:
        min_range = i[0]
        max_range = i[1]

        # if our min is above the previous max range then we just add
        if prev_max < min_range:
            added = max_range - min_range + 1
            prev_max = max_range

        # if its equal then we can also just add but not include the overlap
        elif prev_max == min_range:
            added = max_range - min_range
            prev_max = max_range

        # else we have to deal with the fact that there is an overlap
        else:
            # case 1: our max is also below the prev max so nothing added
            if max_range <= prev_max:
                added = 0
            # case 2: the max is above so we take the difference
            else:
                added = max_range - prev_max
                prev_max = max_range

        num_fresh += added

        if debug:
            print(f"min: {min_range}")
            print(f"max: {max_range}")
            print(f"added: {added}")
            print(f"total: {num_fresh}")
            print()
            print(f"prev max: {prev_max}")


    return num_fresh


def fresh_check(check_ids: list[str], id_lookup: list[tuple[int, int]]):
    fresh = []
    for id in check_ids:
        for lookup in id_lookup:
            if lookup[0] <= int(id) and int(id) <= lookup[1]:
                fresh.append(id)
                break

    return fresh

def all_fresh(id_lookup: list[tuple[int, int]]):
    num_fresh = 0
    for lookup in id_lookup:
        num_fresh += lookup[1] - lookup[0] + 1

    return num_fresh

if __name__ == "__main__":
    main()
