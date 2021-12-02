
import numpy as np

input = np.loadtxt("day1_input.txt")
diff = np.diff(input)
increased = diff > 0 
count_increased = np.sum(increased)
print(count_increased)

