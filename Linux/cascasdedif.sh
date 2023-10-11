#!/bin/bash

# cascasded if sample syntax:
#
# if [ condition1 ]
# then
#	<code 1>
# elif [ condition 2 ]
# then
# 	<code 2>
# ........
# ........
# elif [ condition n ]
#	<code n>
# else
# 	<code n+1>
# fi

# Req: Read student name from STDIN
# capture student mark from argument
# Determine and show the grade based on the mark
# possible grades: HD, D, C, P, Z

read -p "Student name: " name

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


