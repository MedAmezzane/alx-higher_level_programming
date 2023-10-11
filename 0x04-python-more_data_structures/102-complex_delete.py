#!/usr/bin/python3
def complex_delete(prmDictionary, prmValue):
    new_dictionary = {
        key: value
        for key, value in prmDictionary.items()
        if value != prmValue
    }
    return new_dictionary
