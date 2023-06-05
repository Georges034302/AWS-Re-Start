#!/bin/bash

# read a file content line by line
# display the file content line by line
# filename is the first argument of the script

# filename=$1

# read the content of the file using white-space as delimeter
# for line in `cat $filename`; do
# 	echo $line
# done

# read the content of the file using \n as delimeter
while IFS= read -r line; do
	echo $line
done < "$1"	# redirect the content of the file from STDIN