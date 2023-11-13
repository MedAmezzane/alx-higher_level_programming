#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate.
        y (int): The y-coordinate.
        id (int): The identity of the square.

    Args:
        size (int): The size of the square.
        x (int, optional): The x-coordinate. Defaults to 0.
        y (int, optional): The y-coordinate. Defaults to 0.
        id (int, optional): The identity of the square. Defaults to None.

    Properties:
        size: Get or set the size of the square.

    Methods:
        update(self, *args, **kwargs): Update the square's attributes.
        to_dictionary(self): Return the dictionary representation of the square
        __str__(self): Return a string representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The identity of the new Square. Def to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square.

        Returns:
            str: A string with the square's information.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update the Square's attributes.

        Args:
            *args (int): New attribute values in the order (id, size, x, y).
            **kwargs (dict): New attribute key-value pairs.
        """
        if args and len(args) != 0:
            arg_num = 0
            for arg in args:
                if arg_num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_num == 1:
                    self.size = arg
                elif arg_num == 2:
                    self.x = arg
                elif arg_num == 3:
                    self.y = arg
                arg_num += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square.

        Returns:
            dict: A dictionary with the square's attributes.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
