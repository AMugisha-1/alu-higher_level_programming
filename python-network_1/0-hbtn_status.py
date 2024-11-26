#!/usr/bin/python3
"""
Script to fetch and display status information using urllib.
Fetches data from a given URL and prints the X-Request-Id header.
"""

import urllib.request

url = 'https://intranet.hbtn.io/status'

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
