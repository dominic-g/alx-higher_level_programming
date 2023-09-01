#!/usr/bin/python3
import requests
import sys


def get_header():
    """get_header"""
    result = requests.get(sys.argv[1])

    print(result.headers.get("X-Request-Id", None))

if __name__ == "__main__":
    get_header()
