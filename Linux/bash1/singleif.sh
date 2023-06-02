#!/bin/bash

#single if-statement

# if [ logical condition ]
# then
#     <code - commands>
# fi

# read a value from STDIN and check if the value is George
echo -n "Name: "
read name

if [ $name == "George" ]
then
	echo "Welcome George"
fi

echo "good bye!"