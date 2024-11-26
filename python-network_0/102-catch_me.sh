#!/bin/bash
# This script uses curl to send a GET request to the server and handle the response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
