#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    """computes the square value of integers in a matrix"""

    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
