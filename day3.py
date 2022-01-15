

import numpy as np
from numpy.core.numeric import count_nonzero

with open("input.txt") as f:
    text = f.read()

nums = [list(map(int, list(a))) for a in text.splitlines()]

def calc_most_common_digit(array, num_entries):
    return '1' if count_nonzero(array)  >= num_entries / 2 else '0'

def calc_least_common_digit(array, num_entries):
    return '0' if count_nonzero(array) >= num_entries / 2 else '1'

num_rows = len(nums[0])

digits = []

for i in range(num_rows):
    if len(nums) > 1:
        matrix = np.transpose(np.asarray(nums))
        value = calc_most_common_digit(matrix[i], len(nums))
        nums = [entry for entry in nums if entry[i] == int(value)]

# reset nums
nums2 = [list(map(int, list(a))) for a in text.splitlines()]
digits = []

# calculate CO2 scrubber rating
for i in range(num_rows):
    if len(nums2) > 1:
        matrix = np.transpose(np.asarray(nums2))
        value = calc_least_common_digit(matrix[i], len(nums2))
        nums2 = [entry for entry in nums2 if entry[i] == int(value)]

rating1 = "".join([str(i) for i in nums[0]])
rating2 = "".join([str(i) for i in nums2[0]])

num1 = int(rating1, 2)
num2 = int(rating2, 2)

print(num1 * num2)


