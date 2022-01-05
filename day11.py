from functools import reduce
import numpy as np

with open("input.txt", "r") as f:
    data = f.read()

n = 10

lines = np.asarray([np.asarray(list(str(row))) for row in data.split("\n")], dtype=int)
print(lines)

print(lines[0][1])

def is_coord_valid(this_coord):
    return (this_coord >= 0 and this_coord < n)

def adjacent_coords(row, col):
    displacement = [-1, 0, 1]
    rows = [row + i for i in displacement if is_coord_valid(row + i)]
    cols = [col + i for i in displacement if is_coord_valid(col + i)]
    coords = [(row, col) for row in rows for col in cols]
    return coords

def flash_coords(lines, row, col, existing_coords):
    coords_list = adjacent_coords(row, col)
    # turn into matrix
    for row, col in coords_list:
        lines[row][col] = lines[row][col] + 1
        if lines[row][col] == 10:
            existing_coords.append((row, col))

print(adjacent_coords(0, 0))

n_iterations = 500
total_flashes = 0
it = 0
while it < n_iterations and total_flashes != 100:
    total_flashes = 0
    # increment
    lines = lines + np.ones((n,n), dtype = int)
    # flash
    flash = [(i, j) for i in range(n) for j in range(n) if lines[i][j] > 9]
    while len(flash) > 0:
        total_flashes = total_flashes + 1
        row, col = flash.pop()
        flash_coords(lines, row, col, flash)
    lines[lines > 9] = 0
    it = it + 1

print(lines)
print(it)