
# %% part 1 and 2 together

import numpy as np

data_file = "day6_input.txt"

check_days = [80, 256]
max_age = 8

def get_num_of_fish(stock):
    return np.sum(stock)

fish_at_start = np.loadtxt(data_file, delimiter=",", dtype=np.int8)
stock = np.zeros(max_age + 1, dtype=np.uint64)

for fish in fish_at_start:
    stock[fish] += 1

for day in range(1,max(check_days)+1):

    # check number of spawning fish
    spawning_fish = stock[0]

    # advance time
    stock[0:max_age] = stock[1:max_age+1]

    # add new fish, reset spawning fish
    stock[max_age] = spawning_fish
    stock[6] += spawning_fish

    if day in check_days:
        print(f"Day {day}, number of fish: {get_num_of_fish(stock)}")

#%% part 1 (old version)
import numpy as np

data_file = "day6_input.txt"

max_days = 80

def get_num_of_fish(fish):
    return np.sum(fish >= 0)

def print_state(day, fish):
    print(f"Day {day}: ")
    print(fish[fish >= 0])

fish_at_start = np.loadtxt(data_file, delimiter=",", dtype=np.int8)

num_of_fish = len(fish_at_start)
max_num_of_fish = num_of_fish*2**(max_days//7) # estimate 

fish = -1*np.ones(max_num_of_fish, dtype=np.int8)
fish[0:num_of_fish] = fish_at_start

get_num_of_fish(fish)

for day in range(max_days):

    print_state(day, fish)

    # check where 0 is reached
    spawning_idx = np.argwhere(fish == 0)
    num_of_new_fish = len(spawning_idx)

    # advance the time
    fish[0:max_num_of_fish] -= 1

    # reset timer for parent fish
    fish[spawning_idx] = 6 

    # add new fish
    fish[num_of_fish:num_of_fish + num_of_new_fish] = 8
    num_of_fish += num_of_new_fish

print(f"Part 1: {get_num_of_fish(fish)}")