#!/bin/bash
# Script to test if a route accepts the DELETE HTTP method
curl -sX DELETE "$1"
