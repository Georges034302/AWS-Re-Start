#!/bin/bash

# if-else statement

# if [ logical condition ]
# then
#     	<code 1>
# else
# 		<code 2>
# fi

# read a number from STDIN and check if the value is greater than 10
echo -n "n = "
read n

if [ $n -gt 10 ]
then
	echo "$n is greater than 10"
else
	echo "$n is less or equal to 10"
fi

echo "good bye!"