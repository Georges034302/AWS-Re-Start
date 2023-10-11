#!/bin/bash

# while-loop syntax:
#
# while [ condition ]
# do
#	<code repeated>
# 	<iterate condition value>
# done

#Req: 	read a positive integer n from STDIN
#	show every value and its square from 1 to n

read -p "N = " n

i=1

while [ $i -le $n ]
do
	echo "$i --> $(($i*$i))"
	((i++))
done


