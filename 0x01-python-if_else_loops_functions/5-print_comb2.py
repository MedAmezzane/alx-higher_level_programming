#!/usr/bin/python3
# Author - Med.AMEZZANE
# Prints numbers from 0 to 99, with leading zeros for numbers less
# than 10, and separates them with commas.
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
