#%%
import numpy as np

data_file = "day4_input.txt"

draws = np.genfromtxt(data_file, max_rows=1, delimiter=",", dtype=int)
data = np.genfromtxt(data_file, skip_header=2, dtype=int)

rows, cols = data.shape
data = data.reshape((-1,cols,cols))
hits = 0*np.ones_like(data, dtype=int)

no_of_tickets, rows, cols = data.shape

first_winner_found = False
all_found = False
winning_tickets = 0*np.ones(no_of_tickets, dtype=int)
winners = []

for num in draws:

    if not all_found:
        hits[data==num] = 1
        
        for ticket_idx in range(no_of_tickets):
            col_sum = np.sum(hits[ticket_idx,:,:], axis=0)
            row_sum = np.sum(hits[ticket_idx,:,:], axis=1)

            if np.any(col_sum==rows) or np.any(row_sum==cols):
                # print(f"BINGO, ticket no.: {ticket_idx}, draw: {num}")
                winning_tickets[ticket_idx] = 1
                winners.append(ticket_idx)

                if not first_winner_found:
                    print("Solution for part 1 (first winner):")
                    print((np.sum(data[ticket_idx, hits[ticket_idx,:,:]==0]))*num)
                    first_winner_found = True

            if np.all(winning_tickets):

                print("Solution for part 2 (last winner):")
                print((np.sum(data[ticket_idx, hits[ticket_idx,:,:]==0]))*num)
                all_found = True
                break
