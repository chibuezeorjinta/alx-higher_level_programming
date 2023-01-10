#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) and returns the number of characters written:"""
def write_file(filename="", text=""):
	"""
	Args:
		filename = file to which the string is to be writen to.
		text = String to be appended to 'filename',

	Return:
		Number of characters written (output of 'write' object).
	"""
	with open(filename, 'w', encoding="utf-8") as f:
		return f.write(text)
