#!/bin/bash
# Script that sends a POST request using the '-X POST' flag and '-d' to add the data and displays the body response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
