import numpy as np
import functools
import operator

from numpy.lib.twodim_base import diag

with open("input.txt") as f:
    text = f.read()

fish = list(map(int, text.split(',')))
is_first_fish = []

n_days = 256
start_fish = 8
next_fish = 6

old_fish_count = np.zeros((start_fish + 1, 1), dtype=int)
new_fish_count = np.zeros((start_fish + 1, 1), dtype=int)

for i in range(start_fish + 1):
    old_fish_count[i] = fish.count(i)

for i in range(n_days):
    reset_fish = old_fish_count[0] + new_fish_count[0]
    old_fish_count[0:start_fish] = old_fish_count[1:]
    old_fish_count[next_fish] = reset_fish
    new_fish_count[0:start_fish] = new_fish_count[1:]
    new_fish_count[start_fish] = reset_fish

total_fish = np.sum(old_fish_count + new_fish_count)
print(total_fish)