#!/usr/bin/env python3

point1_list = ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']
point2_list = ['D', 'G']
point3_list = ['B', 'C,', 'M', 'P']
point4_list = ['F', 'H', 'V', 'W', 'Y']
point5_list = ['K']
point8_list = ['J', 'X']
point10_dict = ['Q', 'Z']

# point1_dict = dict.fromkeys(point1_list, 1)
# point2_dict = dict.fromkeys(point2_list, 2)
# point3_dict = dict.fromkeys(point3_list, 3)
# point4_dict = dict.fromkeys(point4_list, 4)
# point5_dict = dict.fromkeys(point5_list, 5)
# point8_dict = dict.fromkeys(point8_list, 8)
# point10_dict = dict.fromkeys(point10_dict, 10)

# point_dict = point1_dict | point2_dict | point3_dict | point4_dict | point5_dict | point8_dict | point10_dict

d = {1: point1_list, 2: point2_list, 3: point3_list, 4: point4_list,
     5: point5_list, 8: point8_list, 10: point10_dict}
point_dict = {v: k for k, vs in d.items() for v in vs}

while True:
    word = input('Enter word:')
    if len(word) == 0:
        print('Exit - Bye')
        break
    else:
        word_score = 0
        for char in word:
            # word_score += point_dict[char]
            word_score += point_dict.get(char, 0)
        print(f'{word}: {word_score} points')
