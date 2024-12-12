#!/usr/bin/env python3

# inp = 'python is best'
inp = input('Enter string: ')
ans = {}

for i in inp:
    ans[i] = ans.get(i, 0) + 1

print(ans)
