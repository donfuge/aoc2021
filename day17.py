import numpy as np
from collections import Counter
import re

def preprocess(filename):

    with open(filename,"r") as file:
        target = file.readline().strip()
        limits = [int(x) for x in re.findall(r"\-?\d+", target)]
        xrange = np.arange(limits[0], limits[1] + 1)
        yrange = np.arange(limits[2], limits[3] + 1)

    return xrange, yrange

def solve(data):

    xrange, yrange = data
 
    max_steps = 100
    step = 0

    # velocities to try
    x_velocities = np.arange(1,400)
    y_velocities = np.arange(-300,200)

    results = []
    for x_vel_start in x_velocities:
        # print(x_vel_start)
        for y_vel_start in y_velocities:
            y_max = 0
            x_pos = 0
            y_pos = 0
            step = 0
            x_vel = x_vel_start
            y_vel = y_vel_start
            while (x_pos not in xrange or y_pos not in yrange) and x_pos < max(xrange) and y_pos > min(yrange):
                x_pos += x_vel
                x_vel -= 1*np.sign(x_vel)

                y_pos += y_vel
                y_max = max(y_max, y_pos)
                y_vel -= 1 
            if x_pos in xrange and y_pos in yrange:
                results.append((x_vel_start, y_vel_start, x_pos, y_pos, y_max))

    results.sort(key = lambda x: x[-1]) 
    best = results[-1]
    return len(results), best[-1] 

def part2(data):
    return 

if __name__ == "__main__":

    test_input = preprocess("day17_example.txt")

    example_sol = solve(test_input)
    print(f"Solution for example data: {example_sol}")

    input = preprocess("day17_input.txt")
    sol = solve(input)
    print(f"Solution: {sol}")
