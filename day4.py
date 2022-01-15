import numpy as np
from numpy.core.numeric import count_nonzero

with open("input.txt") as f:
    text = f.read()

n = 5

text_lines = text.split("\n\n")

nums_called = text_lines[0].split(',')

parsed_sheets = []

for sheet in text_lines[1:]:
    sparse_sheet = np.asarray([item for row in sheet.split("\n") for item in row.split(' ') if item is not ''])
    parsed_sheets.append(np.resize(sparse_sheet, (n, n)))

n_sheets = len(parsed_sheets)

np_sheets = np.array(parsed_sheets)

number_sheets = np.zeros((len(np_sheets), n, n), dtype=bool)


def have_won(input_matrix):
    return (n in list(np.sum(input_matrix, 0))) or (n in list(np.sum(input_matrix, 1)))

def how_many_winners(winner_array):
    return len([i for i in winner_array if i])



is_winner = np.ones(len(number_sheets), dtype=bool)
order = np.zeros(len(number_sheets), dtype=bool)
places = 1


for this_num in nums_called:
    contains_called_num = lambda x: x == this_num
    for i in range(n_sheets):
        matches = contains_called_num(parsed_sheets[i])
        number_sheets[i] = np.bitwise_or(matches, number_sheets[i])
        is_winner[i] = have_won(number_sheets[i])
        
    print(is_winner)
    order = [order[i] + places if is_winner[i] and order[i] == 0 else order[i] for i in range(len(order))]
    places = places + 1

    print(how_many_winners(is_winner))
    if (how_many_winners(is_winner) == n_sheets):
        final_num = this_num
        print(final_num)
        print(number_sheets)
        break;

print(order)
index_of_loser = list(order).index(np.max(order))
print(index_of_loser)

print(number_sheets[index_of_loser])
print(index_of_loser)

def calc_score(bingo_sheet, binary_sheet, winning_number):
    numbers = np.array([int(bingo_sheet[i,j]) for i in range(n) for j in range(n) if not binary_sheet[i, j] ])
    print(numbers)
    total = np.sum(numbers)
    print(total)
    return total * winning_number

score = calc_score(parsed_sheets[index_of_loser], number_sheets[index_of_loser], int(final_num))
print(this_num)
print(score)