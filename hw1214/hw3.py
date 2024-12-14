#!/usr/bin/env python3


def curving(in_list):
    # out_list = []
    # for i in in_list:
    #     out_list.append(round(num ** 0.5 * 10))
    # return out_list
    return [round(num ** 0.5 * 10) for num in in_list]


inlist = [89, 77, 95, 81, 100]
print(curving(inlist))
