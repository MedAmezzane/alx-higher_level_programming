#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by ALX."""


import math


class MagicClass:
    """Represent a circle with a magic radius.

    Attributes:
        __radius (float or int): The radius of the MagicClass.
    """

    def __init__(self, radius=0):
        """Initialize a MagicClass with a specified radius.

        Args:
            radius (float or int, optional): The radius of the new MagicClass.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the MagicClass.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
