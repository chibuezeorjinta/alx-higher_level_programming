#!/usr/bin/python3
"""  
	account for errors
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv


def error():
    """ sends a request to the URL and displays the error message """
    url = argv[1]
    try:
        with urlopen(url) as response:
            page = response.read()
        print(page.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    error()
