#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is None:
        return None

    if len(my_list) == 0:
        return None

    max_value = my_list[0]  # Assume the first element is the maximum

    for value in my_list:
        if value > max_value:
            max_value = value  # Update max_value if a larger value is found

    return max_value
