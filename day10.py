from typing import Deque
import numpy as np
from scipy.ndimage import measurements

def preprocess(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
    return lines

opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]

closing_pair_of = {"(": ")",
            "[": "]",
            "{": "}",
            "<": ">"}

def part1(lines):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    part1_sol = 0

    for row in lines:
        env = Deque()
        for char in row:
            if char in opening:
                env.append(closing_pair_of[char])
            if char in closing and not char == env.pop():
                part1_sol += points[char]
                break
    
    return part1_sol


def part2(lines):

    points = {")": 1, "]": 2, "}": 3, ">": 4}

    row_scores = []

    for row in lines:
        env = Deque()
        corrupted = False
        for char in row:
            if char in opening:
                env.append(closing_pair_of[char])
            elif char in closing and not char == env.pop():
                corrupted = True
                break # corrupted line, skip it

        # missing characters at the end of line:
        if not corrupted:
            row_scores.append(0)
            while env:
                bracket = env.pop()
                row_scores[-1] *= 5
                row_scores[-1] += points[bracket]

    num_lines = len(row_scores)
    part2_sol = sorted(row_scores)[num_lines//2]
    return part2_sol

if __name__ == "__main__":

    test_input = preprocess("day10_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 26397

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 288957

    input = preprocess("day10_input.txt")
    part1_sol = part1(input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input)
    print(f"Part 2 solution: {part2_sol}")