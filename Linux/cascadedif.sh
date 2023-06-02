#!/bin/bash

# cascaded if-else statement

# if [ condition1 ]
# then
#     	<code 1>
# elif [ condition 2 ]
# 		<code 2>
# elif [ condition 3 ]
#		<code 3>
# else
#		<code 4>
# fi

# read a student name from STDIN 
# capture student mark from argument
# determine and show the grade based on the mark

echo -n "Student name: "
read name

if [ $1 -ge 85 ]
then
	grade="HD"
elif (($1 >= 75)) 
then
	grade="D"
elif [ $1 -ge 65 ]
then
	grade="C"
elif [ $1 -ge 50 ]
then
	grade="P"
else
	grade="Z"
fi

echo "$name mark is $1 and grade is $grade"

