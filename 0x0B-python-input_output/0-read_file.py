#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout:"""
def read_file(filename=""):
	"""
	collects filename and returns file object.
	Args:
		filename = given filename.

	Return:
		f = open file object.
	"""
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end="")
