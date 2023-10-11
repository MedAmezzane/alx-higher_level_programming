#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of score-weight tuples.

    Args:
        my_list (list): A list of (score, weight) tuples.

    Returns:
        float: The weighted average, or 0 if the list is empty.
    """
    total_score = 0
    total_weight = 0

    if not my_list:
        return 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
