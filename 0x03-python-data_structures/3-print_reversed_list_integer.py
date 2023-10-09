#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        return None

    if not my_list:
        return None

    for number in reversed(my_list):
        print("{:d}".format(number))
