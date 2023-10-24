#!/usr/bin/python3
"""Defines a Square class representing a 2D square shape."""


class Square:
    """A class to create and manipulate square objects.

    Attributes:
        size (int, optional): The size (side length) of the square.
        position (tuple, optional): The position of the square when printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object with a specified size and position.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position of the square when printed.

        Raises:
            TypeError: If size is not an integer, or if position is not a tuple of two integers.
            ValueError: If size is less than 0, or if any value in position is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """The getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """The getter for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """The setter for the position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two integers.
            ValueError: If any value in the tuple is less than 0.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square object with a specified size and position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(' ', end='')
            for _ in range(self.__size):
                print('#', end='')
            print()

    def __str__(self):
        """Return a string representation of the square object.

        Returns:
            str: A string representing the square.
        """
        square = []
        if self.__size == 0:
            return ''

        for _ in range(self.__position[1]):
            square.append('\n')

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                square.append(' ')
            for _ in range(self.__size):
                square.append('#')
            if _ != self.__size - 1:
                square.append('\n')
        return ''.join(square)
