#!/bin/bash

# A dry spell is the number of days with zero rain.

# Determine and show the longest dry spell until -1 is entered from STDIN.

# echo -n "Rainfall: "
# read rain

read -p "Rainfall: " rain 

count=0
max=0

while [[ $rain -ne -1 ]]; do
	if [[ $rain -eq 0 ]]; then
		((count++))
	else
		max=$count
		count=0
	fi
	read -p "Rainfall: " rain
done

if [[ $count -gt $max ]]; then
	max=$count
fi
echo "Longest dry spell = $max"
