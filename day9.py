import numpy as np
import functools
import operator

from numpy.lib.twodim_base import diag

with open("input.txt") as f:
    text = f.read()

lines = text.splitlines()

lines = np.asarray(lines)

counts = 0

x_len = len(lines[0])
y_len = len(lines)

def compare_x(j, i):
    is_min = True
    xij = int(lines[j][i])
    if (i < (x_len - 1)):
        is_min = is_min and ((int(lines[j][i+1]) - xij) > 0)
        if (is_min):
            coords.append((j, i+1))
    if (i > 0):
        is_min = is_min and ((xij - int(lines[j][i-1])) < 0)
        if (is_min):
            coords.append((j, i - 1))
    return is_min, coords

def compare_y(j, i):
    is_min = True
    coords = []
    xij = int(lines[j][i])
    if (j < (y_len - 1)):
        delta1 = (int(lines[j+1][i]) - xij)
        is_min = is_min and (delta1 > 0)
        if (is_min):
            coords.append((j+1, i))
    if (j != 0):
        delta2 = (int(lines[j-1][i]) - xij)
        is_min = is_min and (delta2 > 0)
        if (is_min):
            coords.append((j-1, i))
    return is_min, coords

coords = []

for i in range(x_len):
    for j in range(y_len):
        is_lowest, _ = compare_x(j, i) 
        is_lowest, _ = is_lowest and compare_y(j, i)
        if (is_lowest):
            #count = count + 1 + int(lines[j][i])
            coords.append((j,i))

print(coords)

# Check pool size
for pool_lowest in coords:
        