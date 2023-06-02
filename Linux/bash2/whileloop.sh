#!/bin/bash

# while-loop
# start
# while [start < sentinel]     condition to stop the loop
# do
#	<code>
#   iterate-start
# done
#

echo -n "n = "
read n

i=0

while [ $i -lt $n ]
do
	if [ $(($i%2)) == 0 ] # only show the even numbers
	then
		echo $i 
	fi
	((i++))	# increment i  at every turn to avoid infinite loop
done