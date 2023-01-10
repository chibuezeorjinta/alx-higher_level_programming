#!/usr/bin/python3
"""Write a function that creates an Object from a "JSON file":"""
import json

def load_from_json_file(filename):
	"""
	A function to load object from a file
	Args:
		filename = file to load from.
	Return:
		return an an object using json.load
	"""
	with open(filename, 'r', encoding="utf-8") as f:
		return json.load(f)
