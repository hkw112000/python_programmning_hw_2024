#!/usr/bin/env python3

inp = input('')
# inp = '3215'
# inp = '1110'
res = int(inp)
ans = []

while res != 6174:
    min_list = sorted(list(f'{res:04d}'))
    max_list = min_list[::-1]
    min_number = int(''.join(min_list))
    max_number = int(''.join(max_list))
    res = max_number - min_number
    print(f'{max_number:04d} - {min_number:04d} = {res:04d}')
    ans.append(res)

print(inp, ans)
