import numpy as np
from scipy.ndimage import measurements

def preprocess(filename):
    data = np.genfromtxt(filename, delimiter=1, dtype=np.uint)
    return data

# modified https://stackoverflow.com/questions/3986345/how-to-find-the-local-minima-of-a-smooth-multidimensional-array-in-numpy-efficie
def local_minima(array2d):
    return ((array2d < np.roll(array2d,  1, 0)) &
            (array2d < np.roll(array2d, -1, 0)) &
            (array2d < np.roll(array2d,  1, 1)) &
            (array2d < np.roll(array2d, -1, 1)))

def part1(heightmap):
    heightmap = np.pad(heightmap, 1, mode="maximum")
    lowpoints = local_minima(heightmap)
    lowpoints[[0,-1],...] = False
    lowpoints[..., [0, -1]] = False
    sum_lowpoints = np.sum(heightmap[lowpoints] + 1)
    return sum_lowpoints

def part2(heightmap):
    heightmap += 1
    heightmap[heightmap==10] = 0
    basins_map, num = measurements.label(heightmap)
    basins, counts = np.unique(basins_map, return_counts=True)
    counts = np.sort(counts)[::-1]
    return np.prod(counts[1:4])

if __name__ == "__main__":

    test_input = preprocess("day9_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 15

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 1134

    input = preprocess("day9_input.txt")
    part1_sol = part1(input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input)
    print(f"Part 2 solution: {part2_sol}")