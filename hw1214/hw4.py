#!/usr/bin/env python3

def maxnum(num_str):
    return int(''.join(sorted(list(num_str), reverse=True)))


def minnum(num_str):
    return int(''.join(sorted(list(num_str))))


def process_difference(num_str):
    while True:
        max_val = maxnum(num_str)
        min_val = minnum(num_str)
        diff = max_val - min_val
        print(f"{max_val} - {min_val} = {diff}")
        if diff == 495:
            break
        num_str = str(diff)


inp = input('Enter string: ')
# inp = '251'

print(maxnum(inp))
print(minnum(inp))
process_difference(inp)
