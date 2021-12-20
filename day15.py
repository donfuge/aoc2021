import numpy as np
import heapq
import time

# A* implementation adapted from https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc
# and https://github.com/Chrisbelefantis/A-Star-Algorithm/blob/master/Astar-Algorithm.py

def preprocess(filename):
    map = np.genfromtxt(filename, delimiter=1, dtype=np.uint)
    return map

def manhattan(x1,x2,y1,y2):
    return np.abs(x1-x2) + np.abs(y1-y2)

def geth(map):
    rows, cols = map.shape

    h = np.zeros_like(map, dtype=np.uint)

    for row in range(rows):
        for col in range(cols):
            h[row,col] = manhattan(row, rows-1, col, cols-1)
            
    return h

def get_reversed_path(start, position, came_from, g_score):

    total_path = []
    x, y = position
    score = g_score[x, y]
    while (x,y) != start:
        total_path.append((x,y))
        x, y = came_from[x][y]

    score -= g_score[start[0], start[1]]
    return score, total_path[::-1]

def astar(map, start, end):
    rows, cols = map.shape
    g_score = np.inf * np.ones_like(map, dtype=np.uint)
    f_score = np.inf * np.ones_like(map, dtype=np.uint)
    h_score = geth(map)
    came_from = np.empty(shape=(rows,cols), dtype="i,i")

    g_score[start[0], start[1]] = map[start[0], start[1]]
    f_score[start[0], start[1]] = g_score[start[0], start[1]] + h_score[start[0], start[1]]

    open_list = []

    heapq.heapify(open_list) 
    heapq.heappush(open_list, (f_score[start[0], start[1]], start[0], start[1]))

    deltas = ((0, -1), (0, 1), (-1, 0), (1, 0),)

    while len(open_list) > 0:

        # get the best node
        current_node = heapq.heappop(open_list)
        f, current_x, current_y = current_node

        # check if goal is found
        if (current_x, current_y) == end:
            return get_reversed_path(start, (current_x, current_y) , came_from, g_score)

        for delta in deltas: 

            # adjacent new position
            x, y = (current_x + delta[0], current_y + delta[1])

            # check if inside range
            if x > (rows - 1) or x < 0 or y > (cols - 1) or y < 0:
                continue

            tentative_g = g_score[current_x, current_y] + map[x, y]

            if tentative_g < g_score[x, y] :
                came_from[x, y] = (current_x, current_y)
                g_score[x, y] = tentative_g
                f_score[x, y] = g_score[x, y] + h_score[x, y]

                if (f_score[x, y], x, y) not in open_list:
                    heapq.heappush(open_list, (f_score[x, y], x, y))

    print("could not find the goal")
    return

def visualize_path(map, path):
    path_map = np.zeros_like(map)
    total_risk = 0
    for coords in path:
        total_risk += map[coords[0],coords[1]]
        path_map[coords[0],coords[1]] = total_risk
    print(path_map)
    return

def part1(map):
    rows, cols = map.shape
    start = (0, 0)
    end = (rows - 1, cols - 1)
    start_time = time.time()
    risk, path = astar(map, start, end)
    end_time = time.time()
    print(end_time - start_time)
    visualize_path(map, path)
    return risk

def compare_maps(map, filename):
    extended_map = preprocess(filename)
    return np.all(map == extended_map)

# ugly, but works :)

def extend_map(map):
    extended_1 = np.concatenate((map, shift_map(1, map), shift_map(2, map), shift_map(3, map), shift_map(4, map)), axis=1)
    extended_2 = np.concatenate((shift_map(1, map), shift_map(2, map), shift_map(3, map), shift_map(4, map), shift_map(5, map)), axis=1)
    extended_3 = np.concatenate((shift_map(2, map), shift_map(3, map), shift_map(4, map), shift_map(5, map), shift_map(6, map)), axis=1)
    extended_4 = np.concatenate((shift_map(3, map), shift_map(4, map), shift_map(5, map), shift_map(6, map), shift_map(7, map)), axis=1)
    extended_5 = np.concatenate((shift_map(4, map), shift_map(5, map), shift_map(6, map), shift_map(7, map), shift_map(8, map)), axis=1)
    extended_map = np.concatenate((extended_1, extended_2, extended_3, extended_4, extended_5), axis=0)
    return extended_map

def shift_map(shift, map):
    new_map = np.copy(map)
    new_map += shift
    new_map = (new_map-1) % 9 + 1
    return new_map

def part2(map):
    map = extend_map(np.copy(map))

    rows, cols = map.shape
    start = (0, 0)
    end = (rows - 1, cols - 1)
    start_time = time.time()
    risk, path = astar(map, start, end)
    end_time = time.time()
    print(end_time - start_time)
    visualize_path(map, path)
    return risk

if __name__ == "__main__":

    test_input = preprocess("day15_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 40

    assert compare_maps(extend_map(test_input), "day15_example_ext.txt")

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 315

    problem_input = preprocess("day15_input.txt")
    part1_sol = part1(problem_input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(problem_input)
    print(f"Part 2 solution: {part2_sol}")