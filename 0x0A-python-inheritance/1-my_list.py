#!/usr/bin/python3
"""Inherits from list class"""

class MyList(list):
	
	def print_sorted(self):
		"""prints the list but in ascending order"""
		print(sorted(self))
