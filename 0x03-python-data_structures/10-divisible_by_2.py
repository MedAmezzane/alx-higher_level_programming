#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        return []

    result = []  # Initialize an empty list to store the results
    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
