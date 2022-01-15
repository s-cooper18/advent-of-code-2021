import numpy as np

with open("input_day2.txt") as f:
    text = f.read()

instructions = [a for a in text.splitlines()]

horizontal = 0
depth = 0
aim = 0

for i in instructions:
    commands = i.split(' ')
    word = commands[0]
    distance = int(commands[1])
    if (word[0].startswith('d')):
        aim = aim + distance

    elif (word[0].startswith('u')):
        aim = aim - distance

    else:
        horizontal = horizontal + distance
        depth = depth + aim * distance

print(horizontal)
print(depth)
print(horizontal * depth)
