#!/bin/bash
# script that takes in a URL, sends a request to that URL, using 'awk' get the value of the content length
curl -sI "$1" | awk '/Content-Length/{print $2}'
