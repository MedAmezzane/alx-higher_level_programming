#!/usr/bin/python3
# Author - Med.AMEZZANE

def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - (ord('a') - ord('A')))
        print("{:s}".format(char), end="")
    print("")
