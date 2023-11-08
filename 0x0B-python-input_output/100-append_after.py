#!/usr/bin/python3
"""
Defines a function for inserting text after each line containing a given string
in a text file.
"""


def append_after(filename="", search_string="", new_text=""):
    """Insert text after each line containing a specified string in a text file

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_text (str): The text to insert.
    """
    file_contents = ""
    with open(filename) as file:
        for line in file:
            file_contents += line
            if search_string in line:
                file_contents += new_text
    with open(filename, "w") as updated_file:
        updated_file.write(file_contents)
