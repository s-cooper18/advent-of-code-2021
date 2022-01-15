
import numpy as np
import functools
import operator

from numpy.lib.twodim_base import diag

with open("input.txt") as f:
    text = f.read()

splitlines = text.splitlines()

coords = [line.replace(" -> ", ",").split(",") for line in splitlines]

h_coords = [this_coord for this_coord in coords if this_coord[1] == this_coord[3]]

v_coords = [this_coord for this_coord in coords if this_coord[0] == this_coord[2]]

def is_diag_line(coord):
    delta_x = abs(int(coord[0]) - int(coord[2]))
    delta_y = abs(int(coord[1]) - int(coord[3]))
    return delta_x == delta_y

diag_coords = [this_coord for this_coord in coords if is_diag_line(this_coord)]

line = []

for this_coord in h_coords:
    # if horizontal
    y = int(this_coord[1])
    x1 = int(this_coord[0])
    x2 = int(this_coord[2])
    this_portion = [(x, y) for x in range(min(x1, x2), max(x1,x2) + 1)]
    line.append(this_portion)

print("done h")

for this_coord in v_coords:
    x = int(this_coord[0])
    y1 = int(this_coord[1])
    y2 = int(this_coord[3])
    this_portion = [(x, y) for y in range(min(y1, y2), max(y1,y2) + 1)]
    line.append(this_portion)

print("done v")

for this_coord in diag_coords:
    x = int(this_coord[0])
    delta = abs(int(this_coord[0]) - int(this_coord[2]))
    x_sign = int((int(this_coord[2]) - int(this_coord[0]))/delta)
    y_sign = int((int(this_coord[3]) - int(this_coord[1]))/delta)
    y = int(this_coord[1])
    this_portion = [(x + i * x_sign, y + i * y_sign) for i in range(delta + 1)]
    line.append(this_portion)

print(len(diag_coords))
print(len(v_coords))
print(len(h_coords))

line = functools.reduce(operator.iconcat, line, [])

def return_max(accum, pair):
    m1 = max(int(pair[0]), int(pair[1]))
    return max(accum, m1)

size = functools.reduce(return_max, line, 0) + 1

m = np.zeros((size, size))

# remove
for elem in line:
    m[elem[0]][elem[1]] = m[elem[0]][elem[1]] + 1

print(m)

n = np.array(np.array(m) > 1, dtype=int)
print(np.sum(np.sum(n, 0)))

