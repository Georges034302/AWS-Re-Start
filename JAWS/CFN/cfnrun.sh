#!/bin/bash

function createStack(){
    read -p "Use cfn-template: " stack
    read -p "Create stack: " name
    aws cloudformation create-stack --stack-name $name --template-body file://D:\\GitHub\\AWS-Re-Start\\JAWS\\CFN\\$stack --on-failure DO_NOTHING
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

function deleteStack(){
    read -p "Delete stack: " name
    aws cloudformation delete-stack --stack-name $name
    if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}

function listStacks(){
    aws cloudformation list-stacks --stack-status CREATE_COMPLETE
        if [ $? -eq 0 ]
    then
        echo OK
    else
        echo FAIL
    fi
}
echo -n "CFN command(c/d/l/x): "
read op

while [ "$op" != "x" ]
do 
    case $op in
        "c")createStack
        ;;
        "d")deleteStack
        ;;
        "l")listStacks
        ;;
        *)echo "Unknown command!"
        ;;
    esac
    echo -n "CFN command(c/d/l/x): "
    read op
done

echo
echo "Thank you"
