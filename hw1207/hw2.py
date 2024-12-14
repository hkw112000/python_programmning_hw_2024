#!/usr/bin/env python3

input_list = [3, 5, 6, 1]
ans = {"even": [], "odd": []}

for number in input_list:
    if number % 2 == 0:
        ans["even"].append(number)
    else:
        ans["odd"].append(number)

print(ans)
