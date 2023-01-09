#!/usr/bin/python3
"""Inherits from list class"""

class MyList(list):
	def __init__(self):
		super().__init__()
	
	def print_sorted(self):
		"""prints the list but in ascending order"""
		print(sorted(self))
