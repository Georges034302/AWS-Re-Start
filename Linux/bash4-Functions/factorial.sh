#!/bin/bash

# define the factorial function 
# this function uses a value n from argument
# then returns [using return command] the factorial value of n
# define a procedure called calculate
# calculate will read a value n from STDIN
# then call the factorial function and calculate the factorial of n

function factorial(){
    local n="$1"    # argument value given to the function
    local f=1

    for (( i = 2; i <= $n; i++ )); do
        f=$(($f*$i))
    done
    return $f 
}

function calculate(){
    read -p "n = " n 
    factorial $n    # calculating the factorial of n
    local f=$?      # capture the status of previous command
    echo "Factorial($n) = $f"
}

calculate