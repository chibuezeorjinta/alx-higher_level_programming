#!/usr/bin/python3
"""Write the first class Base"""
class Base:
	"""used to identify each subclass"""
	__nb_objects = 0
	def __init__(self, id=None):
		"""
		initialization
		Args:
			id = Given id. can be inputed but is incremented for each inheritance
		"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
