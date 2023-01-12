#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
        a_dictionary (dictionary): dict to check

    Returns:
        a sorted dictionary
    """
    [print("{}: {}".format(x, a_dictionary[x])) for x in sorted(a_dictionary)]
