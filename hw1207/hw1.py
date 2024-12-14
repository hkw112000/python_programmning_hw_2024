#!/usr/bin/env python3

# inp = 'python is best'
inp = input('Enter string: ')
ans = {}

for char in inp:
    ans[char] = ans.get(char, 0) + 1

print(ans)
