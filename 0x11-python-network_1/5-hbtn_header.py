#!/usr/bin/python3
"""  print the value of X-Request-Id variable found in the header of the response.
"""
import requests
from sys import argv


def get_id():
    """ displays the value of the X-Request-Id variable """
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    get_id()
