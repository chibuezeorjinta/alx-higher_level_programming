#!/bin/bash
# Script that sends a DELETE request to the URL passed and prints the response
curl -s "$1" -X DELETE
