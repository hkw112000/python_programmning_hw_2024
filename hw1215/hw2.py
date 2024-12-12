#!/usr/bin/env python3

input_list = [3, 5, 6, 1]
ans = {"even": [], "odd": []}

for i in input_list:
    if i % 2 == 0:
        ans["even"].append(i)
    else:
        ans["odd"].append(i)

print(ans)
