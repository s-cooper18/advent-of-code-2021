from typing import Any
import numpy as np
import functools
import operator

with open("input.txt") as f:
    text = f.read()

crab_start_pos = np.array([int(i) for i in text.split(',')])

n = len(crab_start_pos)
max_crab_pos = np.max(crab_start_pos)

dists = np.zeros(max_crab_pos, dtype=int)

array_ones = np.ones((len(crab_start_pos)), dtype=int)

map_table = np.zeros(max_crab_pos + 1, dtype=int)
for i in range(1, max_crab_pos + 1):
    map_table[i] = map_table[i-1] + i
print(map_table)

for i in range(1, max_crab_pos + 1):
    index = i - 1
    calc = abs(index * array_ones - crab_start_pos)

    mapped = np.array(list(map(lambda x: map_table[x], calc)), dtype=int)
    dists[index] = np.sum(mapped)

print(dists)


min_pos = np.min(dists)
print(min_pos)

print(list(dists).index(min_pos))
#print(m)
