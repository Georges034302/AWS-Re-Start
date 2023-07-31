#!/bin/bash
# Read template from STDIN
# Read stack-name from STDIN
# Define a function to create a stack (also check the status)
# Define a function to delete a stack (also check the status)
# Define a function to read a stack info (also check the status)
# Define a function to list all cfn stacks (also check the status)
# Define a system menu to offer users (c/r/d/v/x)

function create(){
    echo -n "CFN-template: "
    read template
    echo -n "Stack name: "
    read stack

    aws cloudformation create-stack --stack-name $stack --template-body file://D:\\vsdemo\\cfn\\$template
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

function readStack(){
    echo -n "Stack name: "
    read stack

    aws cloudformation describe-stacks --stack-name $stack
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

function delete(){
    echo -n "Delete stack: "
    read stack

    aws cloudformation delete-stack --stack-name $stack
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

function listStacks(){
    aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

echo -n "CFN command (c/r/d/v/x): "
read cmd

while [ "$cmd" != "x" ]
do
    case $cmd in
        "c")create
        ;;
        "r")readStack
        ;;
        "d")delete
        ;;
        "v")listStacks
        ;;
        *)echo "Unknown command"
        ;;
    esac
    echo -n "CFN command (c/r/d/v/x): "
    read cmd
done
