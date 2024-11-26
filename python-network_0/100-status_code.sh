#!/bin/bash
# This script sends a POST request to a URL.
curl -sI "$1" -o /dev/bull -w "%{http_code}"
