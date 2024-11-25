#!/bin/bash
# sends request to URL passed as argument and displays status code
curl -sI "$1" -o /dev/bull -w "%{http_code}"
