#!/bin/bash

# This is my first script
# I want to assign a value into a variable and display the value
# also I want to create multiple files and lsit them

n=2

echo "n = $n"

touch f{1..5}

ls -l

rm f[0-9]

echo

ls -l
