#!/usr/bin/python3
import urllib.request
import sys


def get_url():
    """get_url"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    get_url()
