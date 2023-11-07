#!/usr/bin/python3
"""
Defines a function for object attribute lookup.
"""


def lookup(obj):
    """
    Return a list of the available attributes of an object.

    Args:
        obj: The object to look up attributes from.

    Returns:
        list: A list of attribute names associated with the object.
    """
    return dir(obj)
