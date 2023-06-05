#!/bin/bash

# read day [0 and 31] and month [0 and 12] from STDIN
# determine the total days from first day of the year
# until the entered day
# [assume there is no leap year]

read -p "Day: " day
read -p "Month: " month

function days(){
	months=(31 28 31 30 31 30 31 31 30 31 30 31)
	local day="$1"
	local month="$2"

	local total=0
	for (( i = 0; i < $month-1; i++ )); do  
		total=$(($total+${months[$i]})) # exp: month = 4---> Jan+Feb+Mar
	done
	total=$(($total+$day)) # day = 4 ---> total days of month +4

	echo $total
}

total=$(days $day $month)
echo "Total days = $total"