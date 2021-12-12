from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def depth_first_search(graph, current_node, visited, twice_used_up):
    visited.add(current_node)
    counter = 0
    for destination in graph[current_node]:
        if destination == "end":
            counter += 1
        elif destination.isupper():
            counter += depth_first_search(graph, destination, set(visited), twice_used_up=twice_used_up)
        elif destination not in visited:
            counter += depth_first_search(graph, destination, set(visited), twice_used_up=twice_used_up)
        elif not twice_used_up and destination != "start":
             counter += depth_first_search(graph, destination, set(visited), twice_used_up=True)

    return counter

def preprocess(filename):
    graph = defaultdict(list)

    with open(filename,"r") as file:
        for line in file:
            source, destination = line.strip().split("-")
            add_edge(graph, source, destination)
            add_edge(graph, destination, source)

    return graph

def part1(graph):
    visited = set()
    starting_node = "start"
    num_paths = depth_first_search(graph, starting_node, visited, twice_used_up=True)

    return num_paths

def part2(graph):
    visited = set()
    starting_node = "start"
    num_paths = depth_first_search(graph, starting_node, visited, twice_used_up=False)

    return num_paths

if __name__ == "__main__":

    test_input = preprocess("day12_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")

    assert part1_example_sol == 226

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")
    assert part2_example_sol == 3509

    input = preprocess("day12_input.txt")
    part1_sol = part1(input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input)
    print(f"Part 2 solution: {part2_sol}")