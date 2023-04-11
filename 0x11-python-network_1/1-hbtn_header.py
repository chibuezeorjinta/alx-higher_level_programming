#!/usr/bin/python3
"""  print the value of X-Request-Id variable found in the header response of a given url.
"""
import urllib.request
from sys import argv


def find_id():
    """ request and print the value of the X-Request-Id variable """
    with urllib.request.urlopen(argv[1]) as response:
        page = response.info()
    print(page['X-Request-Id'])


if __name__ == "__main__":
    find_id()
