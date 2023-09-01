#!/usr/bin/python3
"""0x11. Python - Network #1"""
import requests
import sys


def json_api():
    """json_api"""
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    result = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = result.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    json_api()
