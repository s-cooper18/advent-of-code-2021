import numpy as np
import functools

with open("input.txt") as f:
    text = f.read()

one_len = 2
four_len = 4
seven_len = 3
eight_len = 7

def is_digits_we_care_about(digit):
    len_digit = len(digit)
    digits = [2, 3, 4, 7]
    return len_digit in digits



len_map = {one_len: 1, four_len: 4, seven_len: 7, eight_len: 8}

lines = [line.split(" | ") for line in text.splitlines()]





def string1_in_string2(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True


# Length is 6: 0, 6 or 9

def determine_len_6_num(this_string, one, four):
    if not string1_in_string2(one, this_string):
        return 6

    if not string1_in_string2(four, this_string):
        return 0
    else:
        return 9


# Length is 5: 2, 3 or 5
def determine_len_5_num(this_string, one, six):
    if string1_in_string2(one, this_string):
        return 3
    if string1_in_string2(this_string, six):
        return 5
    else:
        return 2

def map_to_number(number_string, one, four, six):
    this_len = len(number_string)
    if (is_digits_we_care_about(number_string)):
        return len_map[this_len]
    elif this_len == 6:
        return determine_len_6_num(number_string, one, four)
    elif this_len == 5:
        return determine_len_5_num(number_string, one, six)

digits = []

for line in lines:
    left = line[0].split(" ")
    right = line[1].split(" ")
    # Determine 1, 4, 7 and 8

    # are all digits we care about
    easy_digits_sum = np.sum([is_digits_we_care_about(elem) for elem in right])

    right_lens = [len(elem) for elem in right]
    one = [elem for elem in left if len(elem) == one_len][0]
    four = [elem for elem in left if len(elem) == four_len][0]

        #if 6 in right_lens:
            # need to calculate one and four
    mapped_nums = {}
    for elem in left: 
        if len(elem) == 6:
            mapped_nums[determine_len_6_num(elem, one, four)] = elem
    mapped_right = [str(map_to_number(elem, one, four, mapped_nums[6])) for elem in right]
    mapped_left = [str(map_to_number(elem, one, four, mapped_nums[6])) for elem in left]
        
    digit = "".join(mapped_right)

    digits.append(int(digit))

            # need to calc one and six


print(np.sum(digits))


