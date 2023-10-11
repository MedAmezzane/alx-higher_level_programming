#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        return 0

    unique_set = set(my_list)
    total_sum = sum(unique_set)

    return total_sum
