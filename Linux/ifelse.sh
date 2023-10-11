#!/bin/bash

# if-else syntax:
#
# if [ condition ]
# then
#	<code 1>
# else
#	<code 2>
# fi

# Req: Capture integer value from argument
# check if the value is greater or equal to 10, or not

if [ $1 -ge 10 ]
then
	echo "$1 >= 10"
else
	echo "$1 < 10"
fi

echo "Now we finished"
