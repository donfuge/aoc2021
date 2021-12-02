
#%%
import numpy as np

# part 1
input = np.loadtxt("day1_input.txt")

def get_increase_count(data):
    """Returns the number of times the data increases"""
    diff = np.diff(data)
    increased = diff > 0 
    count_increased = np.sum(increased)
    return count_increased

print(get_increase_count(input))

#%%

# part 2

w = 3 # window size
rolling_avg = np.convolve(input, np.ones(w), 'valid') / w

print(get_increase_count(rolling_avg))

# %%
