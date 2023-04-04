#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status using urllib """
import urllib.request


def fetch_status():
    """ https://alx-intranet.hbtn.io/status header """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        page = response.read()
    s = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(s.format(type(page), page, page.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
