#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""


from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from the BaseGeometry class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        string = "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
        return string
