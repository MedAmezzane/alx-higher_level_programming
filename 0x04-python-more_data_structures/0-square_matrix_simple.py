#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        return []

    new_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return new_matrix
