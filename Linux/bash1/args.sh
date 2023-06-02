#!/bin/bash

# Capture the first three arguments given to the script
# Show the script name and the total number of given arguments
# Show the list of all arguments

echo $0 # represents the script
echo $1 # represents the first argument
echo $2 # represents the second argument
echo $3 # represents the third  argument
echo $# # represents the total count of arguments given to the script

echo "Script: $0 has $# arguments"

# $* represents the argument list given to the script
echo "Argument list: $*"