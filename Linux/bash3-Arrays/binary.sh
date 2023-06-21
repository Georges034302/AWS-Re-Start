#!/bin/bash

#Read a decimal between 0 and 255 from STDIN
#Convert the decimal to 8-bits binary 
#Show the binary value

zeroes=(0 0 0 0 0 0 0 0)	# array of 8 zeroes as placeholders
array=()					# holds the results of progressive divisio

length=${#zeroes[@]}		# size 8 binary 

read -p "Decimal: " number	#  read in the decimal value 0 to 255

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

echo "Binary: ${binary[@]}"