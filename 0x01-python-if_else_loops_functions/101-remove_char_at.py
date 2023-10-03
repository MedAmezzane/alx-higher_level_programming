#!/usr/bin/python3
# Author - Med.AMEZZANE

def remove_char_at(input_str, index):
    if index >= 0 and index < len(input_str):
        new_str = input_str[:index] + input_str[index + 1:]
        return new_str
    else:
        return input_str
