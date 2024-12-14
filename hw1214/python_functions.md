1. Write a function palindrome() that takes in a word and return True if word is palindrome and False if not

def palindrome(word):

Sample call:

Enter a word: car
The word car is not a palindrome

Enter a word: racecar
The word racecar is a palindrome

2. Write a function areaT() that takes in 3 sides of a triangle and return the area of the triagnle

def areaT(s1,s2,s3):

3. Write ad function, curving(), that takes in a list of test scores and return the list of curved scores (round to a whole number). The curving algorithm is squre root the raw score, then multiplying by 10.

Sample run:

inlist = [89, 77, 95, 81, 100]

print(curving(inlist))
[94,88,97,90,.100]

4. Write a function maxnum that takes in a 3-digit integer and return the maximum of that integer.

Sample run:
print(maxnum(251))
521

Write a function minnum that takes in a 3-digit integer and return the minimum of that
integer.
Sample run:
Print(minnum(251))
125

Given a 3-digit integer num:
Do until the difference of maxnum and minnum is not 495.

Print the difference (maxnum – minnum)
Sample run:
num = 521
521 – 125 = 396
963 – 369 = 594
954 – 459 = 495
