#!/usr/bin/python3
import random
numb = random.randint(-10, 10)
if numb > 0:
    print(f"{numb:d} is positive")
elif numb == 0:
    print(f"{numb:d} is zero")
else:
    print(f"{numb:d} is negative")
