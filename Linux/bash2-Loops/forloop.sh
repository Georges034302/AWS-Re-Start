#!/bin/bash

# for-loop 
#
# for((start;start < stop;iterate-start))
# do
#	<code>
# done
#

echo -n "n = "
read n

# show i from 0 to n and the i-squared
for((i=0;i<=$n;i++))
do
	pow=$(($i**2))
	echo "$i --> $pow"
done