#!/bin/bash

#Req: Read positive integers from STDIN until -1
# calculate the sum of all values
# determine the maximum entered value
# Show the sum and max

sum=0
max=0

read -p "n = " n

while [ $n -ne -1 ]
do
	sum=$(($sum+$n))

	if [ $n -gt $max ]
	then
		max=$n
	fi

	read -p "n = " n
done

echo "SUM = $sum"
echo "MAX = $max"
