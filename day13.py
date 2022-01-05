import numpy as np

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

fold_steps = data[1].split("\n")

coords = []

for coord in data[0].split("\n"):
    this_coord = coord.split(',')
    coords.append((int(this_coord[0]), int(this_coord[1])))


def fold_up(y_coord, coords):
    for i in range(len(coords)):
        coord = coords[i]
        y = coord[1]
        if y > y_coord:
            new_y = 2*y_coord - y
            coords[i] = (coord[0], new_y)

def fold_left(x_coord, coords):
    for i in range(len(coords)):
        coord = coords[i]
        x = coord[0]
        if x > x_coord:
            new_x = 2*x_coord - x
            coords[i] = (new_x, coord[1])

def do_fold_step(fold_step, coords):
    fold = fold_step.replace("fold along ", "").split('=')
    fold_spot = int(fold[1])
    axis = fold[0]
    print(fold_step)
    print(fold_spot)
    if axis == 'y':
        print("y fold")
        fold_up(fold_spot, coords)
    elif axis == 'x':
        print("x fold")
        fold_left(fold_spot, coords)
    else:
        print("invalid fold")

for step in fold_steps:
    do_fold_step(step, coords)

# convert to immutable

#print(set(coords))
print(len(set(coords)))

final_coords = list(set(coords))

# visualise
x_coords = [coord[0] for coord in final_coords]
y_coords = [coord[1] for coord in final_coords]

max_x = max(x_coords) + 1
max_y = max(y_coords) + 1

print(max_x)
print(max_y)

# empty array
output = np.zeros((max_y, max_x), dtype=int)

print(output.shape)

for i in range(len(x_coords)):
    x = x_coords[i]
    y = y_coords[i]
    output[y][x] = '1'


for i in range(max_y):
    row = ['.'if val == 0 else str(val) for val in output[i]]
    print(" ".join(row))