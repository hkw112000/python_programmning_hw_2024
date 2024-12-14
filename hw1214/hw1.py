#!/usr/bin/env python3

def palindrome(word):
    return word == word[::-1]


inp = input('Enter a word: ')
# if palindrome(inp):
#     print(f"The word {inp} is a palindrome")
# else:
#     print(f"The word {inp} is not a palindrome")
print(f"The word {inp} {'is' if palindrome(inp) else 'is not'} a palindrome")
