#!/usr/bin/python3
"""  post a new email and print the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


def post():
    """send a post to the email variable"""
    url = argv[1]
    values = {'email': argv[2]}
    payload = urllib.parse.urlencode(values)
    payload = data.encode('utf-8')
    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
    print(page)


if __name__ == "__main__":
    post()
