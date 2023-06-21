#!/bin/bash

# Read in a decimal IPv4 from arguments
# Convert the decimal IP to binary IPv4
# show the binary IPv4

echo "IPv4: $1.$2.$3.$4"
ip=($1 $2 $3 $4)		# store the ip decimal octet into array

function convert(){
	zeroes=(0 0 0 0 0 0 0 0)	# array of 8 zeroes as placeholders
	array=()					# holds the results of progressive divisio
	number="${1}"				# give the function an argument
	length=${#zeroes[@]}		# size 8 binary 

	for (( i = 0; i < $length; i++ )); do
		array[$i]=$(($number%2))	# populate array with remainders
		number=$(($number/2))		# update number every iteration
	done

	binary=()
	j=0

	for (( i = $length-1; i >= 0 ; i-- )); do
		binary[$j]=${array[$i]}		# reversing array and storing it into binary
		((j++))
	done

	echo "${binary[@]}"
}

r1=$(convert $1)
r2=$(convert $2)
r3=$(convert $3)
r4=$(convert $4)

echo "Binary IP: $r1.$r2.$r3.$r4"