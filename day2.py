#%% part 1
x = 0
depth = 0

with open("day2_input.txt","r") as file:
    for line in file:
        command = line.split(" ")
        step_size = int(command[1])

        if command[0] == "forward":
            x += step_size
        elif command[0] == "up":
            depth -= step_size
        elif command[0] == "down":
            depth += step_size 

print(x*depth)
# %% part 2

x = 0
depth = 0
aim = 0

with open("day2_input.txt","r") as file:
    for line in file:
        command = line.split(" ")
        step_size = int(command[1])

        if command[0] == "forward":
            x += step_size
            depth += aim * step_size
        elif command[0] == "up":
            aim -= step_size
        elif command[0] == "down":
            aim += step_size 

print(x*depth)
# %%
