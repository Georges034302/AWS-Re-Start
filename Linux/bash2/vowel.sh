#!/bin/bash

# read characters from STDIN until . is entered
# count the total number of vowels
# show the total number of vowels entered

echo -n "character: "
read c 

count=0
while [[ $c != "." ]]; do
	if [[ $c == [aieouAIUOE] ]]; then
		((count++))
	fi

	echo -n "character: "
	read c
done

echo "Vowel count = $count"