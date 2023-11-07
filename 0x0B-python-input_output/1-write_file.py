#!/usr/bin/python3
"""
Defines a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
