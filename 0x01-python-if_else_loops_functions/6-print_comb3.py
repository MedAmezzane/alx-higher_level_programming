#!/usr/bin/python3
# Author - Med.AMEZZANE

for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
