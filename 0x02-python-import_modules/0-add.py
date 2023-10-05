#!/usr/bin/python3
# Author - Med.AMEZZANE

"""Check if this script is executed directly (not imported as a module)"""
if __name__ == "__main__":
	"""Import the 'add' function from the 'add_0' module"""
	from add_0 import add
	"""Define two numbers to be added"""
	a = 1
	b = 2
	"""Calculate the sum using the 'add' function and print the result"""
	print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
