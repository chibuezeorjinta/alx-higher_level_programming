#!/usr/bin/python3
"""  script to get my github ID 
"""
import requests
from sys import argv


def my_github():
    """send get request with embedded authentication"""
    url = "https://api.github.com/user"
    values = (argv[1], argv[2])
    req = requests.get(url, auth=values)
    if req.status_code >= 400:
        print("None")
    else:
        print(req.json().get('id'))


if __name__ == "__main__":
    my_github()
