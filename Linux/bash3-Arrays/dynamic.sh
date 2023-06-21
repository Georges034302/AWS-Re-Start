#!/bin/bash

#create and show a dynamic array of size n [ first argument]

n=$1		# first argument - size of the array

items=()	# creating an empty array

for (( i = 0; i < $n; i++ )); do
	read -p "Item: " item 	# read from STDIN every iteration
	items[$i]=$item 		# store the entry in the array
done

echo "Dynamic array: ${items[@]}"