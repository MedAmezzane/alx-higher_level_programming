#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): Size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Size of a side of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """Calculates the square's area.

        Returns:
            The area of the square.
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter for size attribute.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute.

        Args:
            value (int): The size of a side of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
