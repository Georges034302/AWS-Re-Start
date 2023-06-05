#!/bin/bash

# define a function that generate a sequential array
# define a function that calculates the mean value
# define a select menu that offers the following options:
# 1) show the array
# 2) show the mean
# 3) exit the loop
# 4) unknown commands

declare -A numbers	# declare a global variable array

# function that returns a sequential array
function sample(){
	read n 
	local array=($(seq $n)) # sequence from 1 to n
	echo ${array[@]}		# return thre entire array
}

function mean(){
	local -a array=("$@")	# absorbing array as argument 
	local count=0
	local sum=0
	for e in ${array[@]}; do
		sum=$(($sum+$e))	# calculate the total value
		((count++))			# count how many values
	done
	echo $(($sum/$count))	# the mean value
}

PS3="Choice(1/2/3): "
select choice in array mean x
do
	case $choice in
		array) echo -n "size = "
				numbers=$(sample)
				echo "${numbers[@]}"
		;;
		mean) m=$(mean "${numbers}")
				echo "Mean = $m"
		;;
		x) break
		;;
		*) echo "Unknown command!"
		;;
	esac
done
