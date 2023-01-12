#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurance of any element by another in a new list

    Args:
        my_list : initial list
        search : element to replace in the list
        replace : new element
    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
