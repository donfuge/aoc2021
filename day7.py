import numpy as np

def preprocess(filename):
    data = np.loadtxt(filename, delimiter=",", dtype=np.uint)
    return(data)

def part1(positions):
    x_min = np.min(positions)
    x_max = np.max(positions)
    x0 = np.arange(x_min, x_max + 1) # possible centers

    distances = np.abs(np.tile(positions, (len(x0),1)) - np.tile(x0, (len(positions),1)).T)
    fuels = np.sum(distances, axis=1)
    fuel_min = np.min(fuels)    

    return(fuel_min)

def distance_to_fuel(distance):
    return (1 + distance)/2 * distance

def part2(positions):
    x_min = np.min(positions)
    x_max = np.max(positions)
    x0 = np.arange(x_min, x_max + 1) # possible centers

    distances = np.abs(np.tile(positions, (len(x0),1)) - np.tile(x0, (len(positions),1)).T)
    fuels = np.sum(distance_to_fuel(distances), axis=1)
    fuel_min = np.min(fuels)    

    return(fuel_min)

if __name__ == "__main__":

    test_input = preprocess("day7_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 37

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 168

    input = preprocess("day7_input.txt")
    part1_sol = part1(input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input)
    print(f"Part 2 solution: {part2_sol}")
