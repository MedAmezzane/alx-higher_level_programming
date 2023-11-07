#!/usr/bin/python3
"""
Defines a function for saving a Python object to a JSON file.
"""

import json


def save_to_json_file(obj, filename):
    """
    Save a Python object to a JSON file.

    Args:
        obj (any): The object to save to the file.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, "w") as file:
        json.dump(obj, file)
