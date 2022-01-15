

correct_codes = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf","abcdefg", "abcdfg"]
code_map = {}

for i in range(10):
    code_map[correct_codes[i]] = i


import numpy as np
import functools

with open("input.txt") as f:
    text = f.read()

def subtract(x, y):
    bigger = x if len(x) > len(y) else y
    smaller = y if len(x) > len(y) else x
    if (len(x) - len(y) > 1):
        return smaller
    new_list = list(bigger)
    for letter in smaller:
        if letter in new_list:
            new_list[bigger.index(letter)] = ""
    return "".join(new_list)

parsed_codes = ["".join(sorted(elem)) for elem in text.split(' |')[0].split(' ')]

output_digits = ["".join(sorted(elem)) for elem in text.split(' |\n')[1].split(' ')]


counts = [for digit in output_digits])


print(output_digits)

parsed_code_lens = [len(elem) for elem in parsed_codes]

def determine_possible_nums(index):
    this_len = len(correct_codes[index])
    num = [parsed_codes[i] for i in range(10) if parsed_code_lens[i] == this_len]
    return num



possible_nums = [determine_possible_nums(i) for i in range(10)]
print(possible_nums)


one = possible_nums[1][0]
four = possible_nums[4][0]
seven = possible_nums[7][0]
eight = possible_nums[8][0]

print(one)
print(four)
print(seven)
print(eight)


# Logic
# a = 7 - 1
matches = {}
a = subtract(seven, one)
matches[a] = subtract(correct_codes[7], correct_codes[1])
# only 2 digits are equal

# bd = 4 - 1
bd = subtract(four, one)
matches[bd] = subtract(correct_codes[7], correct_codes[1])

# cdg = 8 - 1
cdg = subtract(eight, one)
matches[cdg] = subtract(correct_codes[8], correct_codes[1])

# determine which is 6

# 0, 6, 9

i = 0
possible = [subtract(possible_nums[i][j], possible_nums[i][j+k]) for j in range(2) for k in range(1, 2)]

# 2, 3, 5
i = 2

sub = subtract(possible_nums[0][0], possible_nums[0][1])
sub2 = subtract(possible_nums[0][2], possible_nums[0][1])
sub3 = subtract(possible_nums[0][2], possible_nums[0][0])

sub4 = subtract(correct_codes[2], correct_codes[3])
print(correct_codes[5], correct_codes[2])
sub5 = subtract(correct_codes[2], correct_codes[5])
sub6 = subtract(correct_codes[3], correct_codes[5])


print(sub, sub2, sub3, sub4, sub5, sub6)


array = possible_nums

