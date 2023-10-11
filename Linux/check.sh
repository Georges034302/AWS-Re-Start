#!/bin/bash

#Req: 	check if an argument is a file or a directory
# 	otherwise ask the user to create a file or directory

if [ -d $1 ]
then
	echo "$1 is a directory"
elif [ -f $1 ]
then
	echo "$1 is a file"
else
	echo "$1 does not exist"
	read -p "Create (f/d): " choice

	if [ "$choice" == "d" ]
	then
		mkdir $1
	elif [ "$choice" == "f" ]
	then
		touch $1
	else
		echo "Unknonwn command"
	fi
fi


