#!/bin/bash

# A procedure is a function with no return value
# A procedure perform an action
# Procedure name is a verb
# Procedure can capture argument same as the script

function show_squares(){
	local n="$1"	# specifies the scope of the variable n within function boundaries

	for (( i = 0; i < $n; i++ )); do
		pow=$(($i*$i))
		echo "$i --> $pow"
	done
	echo
}


show_squares 4
show_squares 8
