#!/bin/bash

# Array is a collection of literal
# Array is ordered
# Array is indexed
# Array allows duplicates

# creating an array items that stores 4 literals
items=(2 hello 3.5 bye)

# determining the array length - how many elements in the array
length=${#items[@]}		# the hash counts the elements
echo "Length of the array = $length"

# displaying the array outright - @ represents all indexes 0 to 3
echo "Array: ${items[@]}"

# accessing array elements by index
for (( i = 0; i < $length; i++ )); do
	echo "Item[$i] = ${items[$i]}"
done
echo

for e in ${items[@]}; do
	echo "$e"
done
echo

j=0
while [[ $j -lt $length ]]; do
	echo "Item[$j] = ${items[$j]}"
	((j++))
done