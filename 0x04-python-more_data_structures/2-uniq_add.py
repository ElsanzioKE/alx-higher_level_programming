#!/usr/bin/python3
def uniq_add(my_list=[]):

    """adds all unique integers in a list (only once for each intege"""

    unique_sum = sum(set(my_list))
    return unique_sum
