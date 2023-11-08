#!/usr/bin/python3
"""
Defines a function for converting an object to a JSON string.
"""

import json


def to_json_string(obj):
    """
    Convert an object to its JSON representation.

    Args:
        obj (any): The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(obj)
