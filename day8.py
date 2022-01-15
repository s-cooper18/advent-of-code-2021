import numpy as np
import functools

with open("input.txt") as f:
    text = f.read()


correct_codes = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg","acf","abcdefg", "abcdfg"]
correct_maps = {}
for i in range(len(correct_codes)):
    correct_maps[correct_codes[i]] = i

correct_code_lens = [len(elem) for elem in correct_codes]
print(correct_code_lens)
print(correct_codes)

# match 2 length]
correct_codes[1]




parsed_codes = text.split(' |')[0].split(' ')
parsed_codes_sorted = ["".join(sorted(elem)) for elem in parsed_codes]
#print([len(elem) for elem in correct_codes])

print(parsed_codes_sorted)

parsed_lens = [len(elem) for elem in parsed_codes_sorted]
print(parsed_lens)

matches = {}

for i in range(1, max(parsed_lens) + 1):
    if i in parsed_lens:
        n = parsed_codes_sorted[parsed_lens.index(i)]
        m = correct_codes[correct_code_lens.index(i)]
        matches[n] = m

print(matches)

for i in range(len(matches)):
    for match in matches:
        



#print(correct_codes)
#print(parsed_codes)

mapped = {}

for i in parsed_codes:
    this_len = len(i)
    mapped[i] = set([code for code in correct_codes if len(code) == this_len])


