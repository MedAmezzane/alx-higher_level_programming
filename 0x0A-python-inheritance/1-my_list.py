#!/usr/bin/python3
"""
Defines a custom list class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    Extends the built-in list class with a method for sorted printing.
    """

    def print_sorted(self):
        """
        Print the list in ascending order after sorting it.
        """
        print(sorted(self))
