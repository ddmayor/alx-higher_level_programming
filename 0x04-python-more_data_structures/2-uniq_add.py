#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list

    Args:
        my_list (list):Defaults to [].
    """
    unique = 0
    for x in set(my_list):
        unique += x
    return unique
