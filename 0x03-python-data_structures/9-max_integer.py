#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_value = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > max_value:
            max_value = my_list[x]
    return (max_value)
