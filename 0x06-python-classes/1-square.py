#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of a side of the square.
    """
    def __init__(self, size):
        """Initializes a square.

        Args:
            size (int): The size of a side of the square.
        """
        self.__size = size
