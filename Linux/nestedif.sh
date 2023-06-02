#!/bin/bash

# nested if-else statement

# if [ condition1 ]
# then
#     	if [ condition2 ]
#		then
#			<code 1>
#		else
#			<code 2>
#		fi
# else
# 		<code 3>
# fi

# read a number from STDIN 
# Check if the value is greater odd, or even, or negative

echo -n "n = "
read n

if [ $n -gt 0 ]
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
