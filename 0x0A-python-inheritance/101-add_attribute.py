#!/usr/bin/python3
"""
Defines a function to add attributes to objects.
"""


def add_attribute(obj, attribute_name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to add an attribute to.
        attribute_name (str): The name of the attribute to add to obj.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, value)
