#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl in silent mode, and displays the size of the body of the response in bytes.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'