#!/bin/bash

# read username and password from STDIN
# ensure that the password is masked on entry
# verify the entries against the credentials "jim" and "123"

read -p "username: " username
read -p "password: " -s password

if [[ $username == "jim" && $password  == "123" ]]; then
	echo -e "\nwelcome $username"
else
	echo -e "\nincorrect credentials!"
fi
