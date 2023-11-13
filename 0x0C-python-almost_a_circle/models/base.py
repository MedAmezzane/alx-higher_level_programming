#!/usr/bin/python3

"""Defines the base model class."""


class Base:
    """Base model.

    This class serves as the foundation for all other classes in Project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identifier for the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
