#!/usr/bin/python3
"""  account for errors
"""
import requests
from sys import argv


def error_rcode():
    """ error management with response module """
    response = requests.get(argv[1])
    code = response.status_code
    if code >= 400:
        print('Error code: {}'.format(status))
    else:
        print(response.text)


if __name__ == "__main__":
    error_rcode()
