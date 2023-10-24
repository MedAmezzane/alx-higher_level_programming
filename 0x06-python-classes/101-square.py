#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square with attributes for size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size (int, optional): The size of the square. Must be >= 0.
            position (tuple, optional): The position of the square when
            printed.
                Must be a tuple of two positive integers.

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                of two positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square. Must be >= 0.

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
        """Gets the position of the square.

        Returns:
            tuple: A tuple of two positive integers defining the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers defining the
            position.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value does not define a valid position.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(v, int) for v in value) or any(v < 0 for v in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square according to its size and position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        square = []
        if self.__size == 0:
            return ''
        for _ in range(self.__position[1]):
            square.append('\n')
        for _ in range(self.__size):
            square.append(' ' * self.__position[0] + '#' * self.__size + '\n')
        return ''.join(square)
