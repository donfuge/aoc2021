import numpy as np
import heapq
import time

# A* implementation adapted from https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc

def preprocess(filename):
    map = np.genfromtxt(filename, delimiter=1, dtype=np.uint)
    return map


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

    def __hash__(self):
        return hash(self.position)

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return current_node.g, path[::-1]  # Return reversed path


def astar(maze, start, end):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    rows, cols = maze.shape
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = set()

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

    # Loop until you find the end
    while len(open_list) > 0:
        # outer_iterations += 1

        # if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
        #   warn("giving up on pathfinding too many iterations")
        #   return return_path(current_node)       
        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (rows - 1) or node_position[0] < 0 or node_position[1] > (cols - 1) or node_position[1] < 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            if new_node not in closed_list and new_node not in open_list:
            # if new_node not in open_list:
                # Append
                children.append(new_node)

        # Loop through children
        for child in children:

            # Create the f, g, and h values
            child.g = current_node.g + maze[child.position[0],child.position[1]]
            child.h = ((child.position[0] - end_node.position[0])  + (child.position[1] - end_node.position[1]) )
            child.f = child.g + child.h

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None

def visualize_path(map, path):
    path_map = np.zeros_like(map)
    total_risk = 0
    for coords in path:
        total_risk += map[coords[0],coords[1]]
        path_map[coords[0],coords[1]] = total_risk
    print(path_map)
    np.savetxt("part2.txt", path_map )

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