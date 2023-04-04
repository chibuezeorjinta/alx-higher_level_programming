#!/bin/bash
# Script that takes an URL and shows the Allowed OPTIONS using some intresting awk
curl -sI -X OPTIONS "$1" | awk '/ALLOW/{print substr($0, index($0,$2))}'
