#!/usr/bin/python3
"""Retrieving url status"""
import urllib.request


def get_url():
    """get_url"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))

if __name__ == "__main__":
    get_url()
