#!/usr/bin/python3
"""
Defines a function for converting a JSON string to a Python object.
"""

import json


def from_json_string(json_string):
    """
    Convert a JSON string to its Python object representation.

    Args:
        json_string (str): The JSON string to convert to a Python object.

    Returns:
        any: The Python object representation of the JSON string.
    """
    return json.loads(json_string)
