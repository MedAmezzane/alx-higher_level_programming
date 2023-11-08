#!/usr/bin/python3
"""
Defines a custom integer class MyInt that inherits from int.
"""


class MyInt(int):
    """
    Custom integer class that overrides the == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality (==) operator to perform inequality (!=)
        comparison.
        """
        return self.real != other

    def __ne__(self, other):
        """
        Override the inequality (!=) operator to perform equality (==)
        comparison.
        """
        return self.real == other
