#!/usr/bin/python3
"""  post with response module
"""
import requests
from sys import argv


def post():
    """sends a POST request to the passed URL with the email using the requests module"""
    url = argv[1]
    values = {'email': argv[2]}
    r = requests.post(url, data=values)
    print(r.text)


if __name__ == "__main__":
    post()
