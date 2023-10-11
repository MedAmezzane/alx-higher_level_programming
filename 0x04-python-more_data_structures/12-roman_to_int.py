#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0

    if roman_string is None or not isinstance(roman_string, str):
        return result

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for index, character in enumerate(roman_string):
        current_value = roman_numerals.get(character, 0)
        next_value = (
            roman_numerals.get(roman_string[index + 1], 0)
            if index + 1 < len(roman_string)
            else 0
        )

        if current_value >= next_value:
            result += current_value
        else:
            result -= current_value

    return result
