#!/usr/bin/python3
"""
Defines a function to convert Python class instance into a JSON representation.
"""


def class_to_json(obj):
    """
    Convert a Python class instance into a JSON-compatible dictionary.

    Args:
        obj: The object to be converted.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
