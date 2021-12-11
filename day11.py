import numpy as np

def preprocess(filename):
    data = np.genfromtxt(filename, delimiter=1, dtype=np.uint)
    return data

def part2(energies):
    rows, cols = energies.shape
    step = 0
    flashed_already = np.zeros_like(energies)

    while not np.all(flashed_already==1):
        energies += 1
        flashes = np.argwhere(energies > 9)
        flashed_already = np.zeros_like(energies)

        while len(flashes):
            for r, c in flashes:
                energies[max(0, r - 1):min(rows, r) + 2, max(0, c - 1):min(cols, c) + 2] += 1
                energies[r,c] = 0
                flashed_already[r, c] = 1

            energies[flashed_already==1] = 0
            flashes = np.argwhere(energies > 9)

        step += 1
    return step

def part1(energies):
    rows, cols = energies.shape
    max_steps = 100
    num_flashes = 0

    for step in range(1, max_steps + 1):
        energies += 1
        flashes = np.argwhere(energies > 9)
        flashed_already = np.zeros_like(energies)

        while len(flashes):
            for r, c in flashes:
                energies[max(0, r - 1):min(rows, r) + 2, max(0, c - 1):min(cols, c) + 2] += 1
                energies[r,c] = 0
                flashed_already[r, c] = 1

            energies[flashed_already==1] = 0
            flashes = np.argwhere(energies > 9)

        num_flashes += np.sum(flashed_already)
    return num_flashes

if __name__ == "__main__":

    test_input = preprocess("day11_example.txt")

    part1_example_sol = part1(test_input.copy())
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 1656

    part2_example_sol = part2(test_input.copy())
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 195

    input = preprocess("day11_input.txt")
    part1_sol = part1(input.copy())
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input.copy())
    print(f"Part 2 solution: {part2_sol}")