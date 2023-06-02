#!/bin/bash

# This script initializes two variables a and b to integers
# Performs arithmetic operations and echo result to STDOUT

a=2
b=3

# using parentheses
result1=$(($a+$b))
echo $result1

# using brackets [ensure there are spaces between the values]
result2=$[ $a + $b ]
echo $result2

# using expr command [ensure there are spaces between the values]
result3=`expr $a + $b`
echo $result3
