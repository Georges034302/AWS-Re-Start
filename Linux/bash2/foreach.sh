#!/bin/bash

# foreach-loop
#
# for [value] in [sequence]
# do
#	<code>
# done
#

# show a sequence of numbers between start and last , jumping (incrementing) by step
# all variables should be entered from STDIN

echo -n "first = "
read first
echo -n "last = "
read last
echo -n "step = "
read step

for e in $(seq $first $step $last)
do
	echo $e
done