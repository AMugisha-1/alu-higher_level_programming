#!/bin/bash
# Script to test if the server supports OPTIONS, HEAD, GET, POST, PUT, DELETE methods
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f2-
