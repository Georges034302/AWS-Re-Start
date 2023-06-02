#!/bin/bash

# case-statement
# 
# case [selection value] in
#	choice1) <command 1>
#	;;
#	choice2) <command 2>
#	;;
#	choice3) <command 3>
#	;;
#	choice4) <command 4>
#	;;
#	choice5) <command 5>
#	;;
# esac


# develop a calculator to perform basic arithmetic operations
# for 2 integers entered from STDIN using case-statement
echo -n "a = "
read a

echo -n "b = "
read b

echo -n "Operation(+ - * /): "
read op

case $op in
	+) let result=$a+$b
		;;
	-) result=$(($a-$b))
		;;
	\*) let result=$a\*$b
		;;
	/) result=$(echo "scale=2;$a/$b" | bc | awk '{printf"%3.2f \n",$0}')
		;;
esac

echo "$a $op $b = $result"