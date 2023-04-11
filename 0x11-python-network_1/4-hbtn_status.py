#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status header """
import requests


def fetch():
    """ fetches https://alx-intranet.hbtn.io/status """
    req = requests.get('https://alx-intranet.hbtn.io/status')
    format = "Body response:\n\t- type: {}\n\t- content: {}"
    print(format.format(type(req.text), req.text))


if __name__ == "__main__":
    fetch()
