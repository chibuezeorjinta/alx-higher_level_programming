#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:"""
def append_file(filename="", text=""):
	"""
	Args:
		filename = file to which the string is to be writen to.
		text = String to be appended to 'filename',

	Return:
		Number of characters written (output of 'write' object).
	"""
	with open(filename, 'a', encoding="utf-8") as f:
		return f.write(text)
