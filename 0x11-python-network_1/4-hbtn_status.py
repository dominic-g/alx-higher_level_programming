#!/usr/bin/python3
"""0x11. Python - Network #1"""
import requests


def get_status():
    """get_status"""
    result = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))

if __name__ == "__main__":
    get_status()
