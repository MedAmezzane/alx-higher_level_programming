#!/usr/bin/python3
"""
Defines a function for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
