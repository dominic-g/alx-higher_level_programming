#!/usr/bin/python3
"""0x11. Python - Network #1"""
import requests
import sys


def post_email():
    """post_email"""
    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})

    print(result.text)

if __name__ == "__main__":
    post_email()
