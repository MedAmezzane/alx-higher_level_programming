#!/usr/bin/python3

"""Defines the base model class."""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_of_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_of_dicts (list): A list of dictionaries.
        """
        if list_of_dicts is None or not list_of_dicts:
            return "[]"
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_file(cls, list_of_objects):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_of_objects (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_of_objects is None:
                jsonfile.write("[]")
            else:
                list_of_dicts = [
                    obj.to_dictionary()
                    for obj in list_of_objects
                    ]
                jsonfile.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Return the deserialization of a JSON string.

        Args:
            json_str (str): A JSON string representing a list of dictionaries.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of class instances instantiated from a JSON file.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated class instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_of_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objects):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_of_objects (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_of_objects is None or not list_of_objects:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_of_objects:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of class instances instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated class instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_of_dicts = [dict([k, int(v)] for k, v in d.items())
                                 for d in list_of_dicts
                                 ]
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#2cb77b")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for _ in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for _ in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
