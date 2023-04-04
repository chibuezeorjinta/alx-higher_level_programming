#!/bin/bash
# Script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -s -I "$1" | awk '/^HTTP/{print $2}'
