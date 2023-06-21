#!/bin/bash

# enter values from STDIN until -1
# calculate the total values entered
# determine the maximum value entered
# show the total and max

echo -n "n = "
read n 

sum=0
max=0

while [ $n -ne -1 ]	# -1 is the sentinal that stops the loop
do
	sum=$(($sum+$n))	# update the sum with every iteration

	if [[ $n -gt $max ]]; then
		max=$n 		# update max with every iteration
	fi

	echo -n "n = "
	read n 
done

echo "SUM = $sum"
echo "MAX = $max"