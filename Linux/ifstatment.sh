#!/bin/bash

# if statement syntax:
#
# if [ condition ]
# then
#	<code>
# fi

# Req: Read integer value from STDIN
# check if the value is greater than 10

echo -n "N = "
read n   # reading value from keyboard

if [ $n -gt 10 ]
then
	echo "$n is greater than 10"
fi # end if statement

echo "Thank you"
