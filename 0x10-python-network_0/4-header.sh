#!/bin/bash
# Script that takes an URL and displays the body of the response while setting a header variable
curl -s "$1" -H "X-School-User-Id: 98"
