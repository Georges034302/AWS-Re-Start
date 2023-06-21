#!/bin/bash

# create and show a sequential array
# the last element is from argument
# calculate and show the sum of even numbers

numbers=($(seq $1)) # $1 represents the last value

echo "Sequential array: ${numbers[@]}"

sum=0

for e in ${numbers[@]}; do
	if [[ $(($e%2)) == 0 ]]; then
		sum=$(($sum+$e))
	fi
done

echo "Even-Sum = $sum"