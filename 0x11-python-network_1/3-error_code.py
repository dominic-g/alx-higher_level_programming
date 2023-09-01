#!/usr/bin/python3
import urllib.request
import urllib.error
import sys


def send_post():
    """send_post"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    send_post()
