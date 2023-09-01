#!/usr/bin/python3
"""0x11. Python - Network #1"""
import sys
import requests


def github_commits():
    """github_commits"""
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    result = requests.get(url)
    try:
        d = result.json()
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except IndexError:
        pass

if __name__ == "__main__":
    github_commits()
