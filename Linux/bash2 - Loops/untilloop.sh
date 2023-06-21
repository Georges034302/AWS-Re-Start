#!/bin/bash

# until-loop
# start
# until [conditon]     until the condition becomes false, execute
# do
#	<code>
#   iterate-start
# done
#

echo -n "n = "
read n

i=0
until [ $i -gt $n ]
do
	if [ $(($i%2)) == 0 ] # only show the even numbers
	then
		echo $i 
	fi
	((i++))	# increment i  at every turn to avoid infinite loop
done