#!/bin/bash

# for-loop syntax:
#
# for((starting value;value<=sentinel;update value))
# do
#	< repeated code>
# done

#Req: 	read a positive integer n from STDIN
#	show all values from 1 to n and their squares
#Syntax I/O: i ---> square of i  (n times)

read -p "N = " n

for((i=1;i<=$n;i++)) # i++  equiv to i = i + 1
do
	echo "$i --> $(($i*$i))"
done


