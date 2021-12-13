import numpy as np
import matplotlib.pyplot as plt

def preprocess(filename):
    
    points = []
    folds = []
    max_num = 0

    with open(filename,"r") as file:
        for line in file:
            if "," in line:
                x, y = [int(num) for num in line.strip().split(",")]
                max_num = max(max_num, x, y) 
                points.append((x, y))
            elif "fold" in line:
                str, num = line.strip().split("=")
                folds.append((str[-1], int(num)))

    paper = np.zeros(shape=(max_num + 1, max_num + 1))

    for point in points:
        x, y = point
        paper[y,x] = 1

    return paper, folds

def fold_up(paper, num):

    rows, cols = paper.shape
    top = paper[0:num,:] 
    bottom = paper[num + 1:,:]

    if len(top) >= len(bottom):
        bottom = np.flipud(bottom)
        top[len(top)-len(bottom):,:] += bottom
        return top[len(top)-len(bottom):,:]
    else:
        top = np.flipud(top)
        bottom[0:len(top),:] += top
        return bottom[0:len(top),:]
     

def part2(data):
    paper, folds = data

    for fold in folds:
        axis, num = fold

        # horizontal
        if axis == "y":
            paper = fold_up(paper, num)
        # vertical
        elif axis == "x":
            paper = fold_up(paper.T, num).T

    plt.imshow(paper >= 1)
    plt.show()
    return np.sum(paper >= 1)

def part1(data):
    paper, folds = data

    fold = folds[0]
    axis, num = fold

    # horizontal
    if axis == "y":
        paper = fold_up(paper, num)
    # vertical
    elif axis == "x":
        paper = fold_up(paper.T, num).T

    return np.sum(paper >= 1)

if __name__ == "__main__":

    test_input = preprocess("day13_example.txt")

    part1_example_sol = part1(test_input)
    print(f"Part 1 solution for example data: {part1_example_sol}")
    assert part1_example_sol == 17

    part2_example_sol = part2(test_input)
    print(f"Part 2 solution for example data: {part2_example_sol}")

    input = preprocess("day13_input.txt")
    part1_sol = part1(input)
    print(f"Part 1 solution: {part1_sol}")

    part2_sol = part2(input)
    print(f"Part 2 solution: {part2_sol}")