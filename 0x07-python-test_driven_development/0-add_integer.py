#!/usr/bin/python3
"""
Defines a function for integer addition.
"""

def add_integer(a, b=98):
    """
    Return the integer addition of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The result of adding `a` and `b` as integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
