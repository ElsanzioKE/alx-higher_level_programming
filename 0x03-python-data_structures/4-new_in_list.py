#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):

    """replaces an element in a specific location"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = new_element
    return new_list
