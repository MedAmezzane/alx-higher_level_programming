#!/usr/bin/python3
# Print all lowercase letters from 'a' (97) to 'z' (122) except 'q' and 'e'.
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
