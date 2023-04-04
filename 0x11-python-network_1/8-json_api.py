#!/usr/bin/python3
""" 
	Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


def setup_json_api():
    """setup a json query api"""
    value = dict()
    if argv[1]:
           value={'q': argv[1]}
    else:
          value={'q': ""}
    url="http://0.0.0.0:5000/search_user"
    postage = requests.post(url, data=value)
    if type(postage.json) is not dict():
          return "Not a valid JSON"
    elif len(postage.json) == 0:
          return "No result"
    else:
          print("[{}] {}").format(postage.json['id'], postage.json['name'])
          
if __name__ == "__main__":
      setup_json_api()