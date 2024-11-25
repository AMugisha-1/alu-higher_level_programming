#!/bin/bash
# sends data from a file and displays response
curl -sX POST "$1" -d @"$2" -H "content-type: application/json"
