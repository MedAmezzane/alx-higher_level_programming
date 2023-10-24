#!/usr/bin/python3
"""Define a singly linked list and node classes"""


class Node():
    """Node class for a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a singly-linked list node.

        Args:
            data (int): The data contained in the node.
            next_node (Node, optional): The next node of the list.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node instance.
        """

        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Get the data value in the current node.

        Returns:
            int: Data value contained in the current node.
        """

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the current node.

        Args:
            value (int): The new data value of the node.

        Raises:
            TypeError: If the data value is not an integer.
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the current node.

        Returns:
            Node: The next_node of the current node.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set a new next_node value for the current node.

        Args:
            value (Node): The new node.

        Raises:
            TypeError: If the next_node is not a Node instance.
        """

        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Singly-linked list class - starts out empty"""

    def __init__(self):
        """Initialize an empty singly linked list object."""

        self.__head = None

    def sorted_insert(self, value):
        """Insert a Node into the linked list in a sorted fashion.

        Args:
            value (int): The Node value.

        Raises:
            TypeError: If the value supplied to the node is not an integer.
        """

        if type(value) != int:
            raise TypeError("data must be an integer")
        temp = None
        iterator = self.__head
        new_node = Node(value)
        if iterator is None:
            new_node.__next_node = None
            self.__head = new_node

        else:
            while iterator is not None and value > iterator.data:
                temp = iterator
                iterator = iterator.__next_node
            if temp is None:
                new_node.__next_node = self.__head
                self.__head = new_node
            else:
                temp.__next_node = new_node
                new_node.__next_node = iterator

    def __str__(self):
        """Default printing operation for the class when print() is called.

        Returns:
            str: The linked list in string format.
        """

        linked_list = []
        iterator = self.__head
        while iterator is not None:
            linked_list.append(iterator.data)
            iterator = iterator.__next_node
        return '\n'.join(str(i) for i in linked_list)
