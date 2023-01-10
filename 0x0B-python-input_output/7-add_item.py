#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list, and then save them to a file:"""
import sys

save_a_json = __import__('5-save_to_json_file').save_to_json_file
load_a_json = __import__('6-load_from_json_file').load_from_json_file

existing_list = []
load_list = []
n = len(sys.argv)
for n in range(1, n):
	load_list = sys.argv[n]
def main():
	"""
	load the json file with what ever is their already.
	convert it back into an object 'list' using json.load.
	add the contents of the new list to the old list.
	convert the loaded list back to json
	"""
	f = "add_item.json"
	try:
		exiting_list = load_a_json(f)
	except FileNotFoundError:
		with open(f, 'w', encoding="utf-8") as new:
			print("Empty file created")
	except ValueError:
		existing_list = []
	existing_list += load_list
	return save_a_json(existing_list, f)
main()
