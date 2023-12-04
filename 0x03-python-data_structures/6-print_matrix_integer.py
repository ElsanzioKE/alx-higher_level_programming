#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """prints a matrix of integers"""

    if not matrix:
        return
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print("$")
