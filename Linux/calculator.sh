#!/bin/bash

# Read two integer values from STDIN
# Show the total value

echo -n "a = "
read a

echo -n "b = "
read b

total=$[ $a + $b ]
echo "$a +$b = $(($a+$b))"

echo "$a + $b = $total"

# Capture 2 integer arguments
# Show the total

result=`expr $1 + $2`

echo "$1 + $2 = $result"

let res=$1-$2
echo "$1 - $2 = $res"
