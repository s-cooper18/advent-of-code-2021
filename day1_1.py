import numpy as np

with open("input.txt") as f:
    text = f.read()

nums = [int(a) for a in text.splitlines()]

nums = [nums[i] + nums[i+1] + nums[i+2] for i in range(len(nums) - 2)]


increase = np.asarray([ 1 if (nums[i + 1] - nums[i]) > 0 else 0 for i in range(len(nums) - 1)])

print(increase.sum())
