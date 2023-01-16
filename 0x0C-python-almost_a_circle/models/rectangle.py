#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
	"""Create Rectangle class with Base class properties"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		Args:
			width = Width of rectange
			height = height of rectange
			x (int) = default 0
			y (int) = default 0
			id = from superclass base
		Raise:
			TypeError for width and height
		"""
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
		super().__init__(id)

	@property
	def width(self):
		"""public getter for width"""
		return self.__width

	@width.setter
	def width(self, width):
		"""public setter for width"""
		if type(width) is not int:
			raise TypeError("width must be an integer")
		
		if width <= 0:
			raise ValueError("width must be > 0")

		self.__width = width

	@property
	def height(self):
		"""public getter for height"""
		return self.__height

	@height.setter
	def height(self, height):
		"""public setter for height"""
		if type(height) is not int:
                        raise TypeError("height must be an integer")
		
		if height <= 0:
			raise ValueError("height must be > 0")

		self.__height = height
	
	@property
	def x(self):
		"""public getter for 'x'"""
		return self.__x
	
	@x.setter
	def x(self, x=0):
		"""public setter for x"""
		if type(x) is not int:
                        raise TypeError("x must be an integer")
		if x < 0:
			raise ValueError("x must be >= 0")
		if x == None:
			self.__x = x
	
	@property
	def y(self):
		"""public getter for 'y'"""
		return self.__y

	@y.setter
	def y(self, y=0):
		"""public setter for y"""
		if type(y) is not int:
                        raise TypeError("y must be an integer")
		if y < 0:
			raise ValueError("y must be >= 0")
		if y == None:
			self.__y = y
	
	def area(self):
		"""Public method to get area"""
		return self.__width * self.__height
	
	def display(self):
		"""display the rectangle using '#' blocks"""
		for h in range(0, self.__height):
			print('#' * self.__width)
	
	def __str__(self):
		"""Overrride default string"""
		return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
	
	def update(self, *args):
		""" Assign args using *args"""
		try:
			self.id = int(args[0])
		except IndexError:
			return
		try:
			self.width = int(args[1])
		except IndexError:
			return
		try:
			self.height = int(args[2])
		except IndexError:
			return
		try:
			self.x = int(args[3])
		except IndexError:
			return
		try:
			self.y = int(args[4])
		except IndexError:
			return
