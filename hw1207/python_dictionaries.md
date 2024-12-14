1. Write a program that asks the user to enter a string (consisting of any characters). Then create and print dictionary from that string whose keys are the characters of the string and whose values are how many times those character apper in the string.

Example:

Enter string: python is best

{'p':1,'y':1,'t':2,'h':1,'o':1,'n':1,' ':2,'i':1,'s':2,'b':1,'e':1}

2. Given a list, create a dictionary with two keys, "even" and "odd". The values associated with each key must be the list of correspongding evfen and odd values in the given list.

input_list = [3,5,6,1]
Prints {"even":[6], "odd":[3,5,1]}

3. Create a list of dictionaries using the data from the elements.txt file.

[{'element':1, 'sysmbol':'H','name':'Hydrogen'}, {'element':2, 'sysmbol':'He','name':'Helium'}, ...]
Search your dictionary for all the elements that do not end with 'ium'.

4. (optional) Kapreka constant, or 6174, is a constant that arises when we take a 4-digit integer, form the largest and smallest numbers from it digits, and then subtract these two numbers.

Write a program to find all the iterations to get to 6174. Print a dictionary with the 4-digit integer as the key and value is a list of the differences(see example).

3215

5321-1235=4086
8640-0468=8172
8712-1278=7443
7443-3447=3996
9963-3699=6264
6642-2466=4176
7641-1467=6174

{3215: [4086,8172,7443,3996,6264,4176,6174]}
Test your code with these number 1234, 1110 and 0999
