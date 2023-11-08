#!/usr/bin/python3
"""
Defines a function to generate Pascal's Triangle of a specified size.
"""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the Pascal's Triangle to generate.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    pascals_triangle = [[1]]
    while len(pascals_triangle) != n:
        current_row = pascals_triangle[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        pascals_triangle.append(new_row)

    return pascals_triangle
