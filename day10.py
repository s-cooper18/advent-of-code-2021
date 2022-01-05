
from functools import reduce

with open("input.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
left_brackets = ['(', '[', '{', '<']
right_brackets = [')', ']', '}', '>']

points = {}
points[right_brackets[0]] = 3
points[right_brackets[1]] = 57
points[right_brackets[2]] = 1197
points[right_brackets[3]] = 25137

points[left_brackets[0]] = 1
points[left_brackets[1]] = 2
points[left_brackets[2]] = 3
points[left_brackets[3]] = 4


def is_valid_line(line):
    old_line = ""
    while old_line != line:
        old_line = line
        for j in range(len(left_brackets)):
            line = line.replace(left_brackets[j] + right_brackets[j], "")
    right_chars = [char for char in line if char in right_brackets]
    if len(right_chars) > 0:
        return (False, line)
    else:
        return (True, line)

def calculate_error_points(chars):
    counts = [points.get(this_char) for this_char in chars]
    return reduce((lambda x, y: x + y), counts)

def calculate_completion_points(chars):
    counts = [points.get(this_char) for this_char in chars]
    counts.reverse()

    return reduce((lambda x, y: 5*x + y), counts)

new_points = []

for this_line in lines:
    valid, fixed_line = is_valid_line(this_line)
    print(valid)
    print(fixed_line)
    if (valid and len(fixed_line) > 0):
        new_points.append(calculate_completion_points(fixed_line))

new_points.sort()

middle_index = len(new_points) // 2
print(middle_index)
print(new_points)
print(new_points[middle_index])
#this_char = "".join([parse_line(this_line) for this_line in lines])
#print(calculate_points(this_char))

