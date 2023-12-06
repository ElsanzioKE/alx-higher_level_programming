#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    """ returns a set of all elements present in only one set."""

    result_set = set()
    for elem in set_1:
        if elem not in set_2:
            result_set.add(elem)
    for elem in set_2:
        if elem not in set_1:
            result_set.add(elem)

    return result_set
