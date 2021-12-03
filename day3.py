
#%% part 1
import numpy as np

with open("day3_input.txt","r") as file:
    all_lines = [line.rstrip() for line in file]

rows = len(all_lines)
cols = len(all_lines[0])

diagnostics = np.zeros((rows, cols), dtype=int)

# convert input data to matrix

for row, line in enumerate(all_lines):
    for col, char in enumerate(line):
        diagnostics[row, col] = int(char)

gamma_mask = np.sum(diagnostics,axis=0) > rows/2 
epsilon_mask = ~gamma_mask

powers_of_two = np.asarray(list(reversed([2**n for n in range(cols)])))

gamma = np.sum(powers_of_two[gamma_mask])
epsilon = np.sum(powers_of_two[epsilon_mask])

print(gamma*epsilon)
# %% part 2

def get_common(matrix, most, pos=0):
    rows, cols = np.shape(matrix)
    if most:
        mask = np.sum(matrix,axis=0) >= rows/2 
    else:
        mask = np.sum(matrix,axis=0) < rows/2 
    common = np.asarray(mask, dtype=int)
    sel_idx = np.argwhere(matrix[:,pos]==common[pos]).flatten()

    if len(sel_idx) == 1:
        powers_of_two = np.asarray(list(reversed([2**n for n in range(cols)])))
        return(np.dot(matrix[sel_idx],powers_of_two))
    else:
        return(get_common(matrix[sel_idx,:], most=most, pos=pos+1))

oxygen = get_common(diagnostics, most=True)
scrubber = get_common(diagnostics, most=False)

print(oxygen)
print(scrubber)

print(oxygen*scrubber)

# %%
