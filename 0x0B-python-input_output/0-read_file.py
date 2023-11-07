#!/usr/bin/python3
"""
Defines a function for reading and printing the contents of a text file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
