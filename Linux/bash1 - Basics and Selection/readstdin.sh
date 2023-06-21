#!/bin/bash

# Read values from STDIN
# show the values to STDOUT

# option n prevent the cursor from jumping to a new line
echo -n "Name: "
read name

echo "Welcome $name"
