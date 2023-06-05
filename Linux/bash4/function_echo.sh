#!/bin/bash

# A function returns a value to the caller
# a function name is a noun

read -p "a = " a 
read -p "b = " b

function total(){
	local a="$1"
	local b="$2"
	echo $(($a+$b))
}

echo "$a + $b = $(total $a $b)"