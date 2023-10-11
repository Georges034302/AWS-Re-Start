#!/bin/bash

# nested-if sample syntax:
#
# if [ condition 1 ]
# then
#	<code 1>
#	if [ condition 2 ]
#	then
#		<code 2>
#	else
#		<code 3>
#	fi
# else
#	<code 4>
# fi

# Red: Read integer value from STDIN
# check if the value is odd, or even, or negative

# echo -n "N = "
# read n

read -p "N = " n # prompt and read same time

if [ $n -ge 0 ]
then
	if [ $(($n%2)) == 0 ]
	then
		echo "$n is even"
	else
		echo "$n is odd"
	fi
else
	echo "$n is negative"
fi




