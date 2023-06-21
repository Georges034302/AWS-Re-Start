#!/bin/bash

# PROMPT
# 
# select [choice] in [sequence]
# do
#	case [$choice] in
#   	choice1) <command1>
#		;;
#	case [$choice] in
#   	choice2) <command2>
#		;;
#	case [$choice] in
#   	choice3) <command3>
#		;;
# 	esac
# done
#

# choice a direction to travel (north,east,south,west)
PS3="Choice: "

select DIRECTION in north east west south x
do
	case $DIRECTION in 
		north) echo "Go to North Sydney over the Harbor Bridge"
		;;
		east) echo "Go to Eastern Suburbs via M1"
		;;
		south) echo "Go to South Sydney via M5"
		;;
		west) echo "Go to West Sydney via M4"
		;;
		x) break
		;;
		*) echo "ERROR: Invalid Direction!"
		;;
	esac
done

