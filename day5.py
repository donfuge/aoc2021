#%% 
import numpy as np

data_file = "day5_input.txt"

with open(data_file,"r") as file:
    data = file.readlines()

no_of_lines = len(data)
start_coords = np.zeros((no_of_lines,2), dtype=int)
end_coords = np.zeros((no_of_lines,2), dtype=int)

for line_idx, line in enumerate(data):
    start, end = line.split("->")
    x0, y0 = start.split(",")
    x1, y1 = end.split(",")

    start_coords[line_idx] = [x0, y0] 
    end_coords[line_idx] = [x1, y1]

map_size = np.max(start_coords[:]) + 1
map = np.zeros((map_size, map_size))
full_map = np.zeros((map_size, map_size))

for line_idx in range(no_of_lines):
    x0, y0 = start_coords[line_idx]
    x1, y1 = end_coords[line_idx]

    if (x0 == x1):
        map[x0, min(y0, y1):max(y0, y1) + 1] += 1
        full_map[x0, min(y0, y1):max(y0, y1) + 1] += 1  
    elif (y0 == y1):
        map[min(x0, x1):max(x0, x1) + 1, y0] += 1
        full_map[min(x0, x1):max(x0, x1) + 1, y0] += 1
    else:
        for x,y in zip(range(x0, x1 + (-1 if x1<x0 else 1) , -1 if x1<x0 else 1), range(y0, y1 + (-1 if y1<y0 else 1), -1 if y1<y0 else 1)):
            full_map[x, y] += 1

print("Part 1")
# print(map)
print(np.sum(map>=2))


print("Part 2")
# print(full_map)
print(np.sum(full_map>=2))

# %%
