#!/usr/bin/python3
"""
Defines a class Student to represent student information and associated methods
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represent only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The list of attribute names to represent.
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {tr: getattr(self, tr) for tr in attrs if hasattr(self, tr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with the values from a
            dictionary.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
