#!/usr/bin/python3
"""
Defines a function for checking if an object is an instance of a specific class
"""


def is_same_class(obj, a_class):
    """
    Check if the type of an object matches a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with the type of obj.

    Returns:
        True if obj's type is exactly the same as a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
