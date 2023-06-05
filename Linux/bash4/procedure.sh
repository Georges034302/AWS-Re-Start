#!/bin/bash

# A procedure is a function with no return value
# A procedure perform an action
# Procedure name is a verb

function show_user(){
	echo "User: $(whoami)"
	ps aux | awk '{print $2}'
}

show_user