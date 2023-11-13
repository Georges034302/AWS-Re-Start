#!/bin/bash
# Define a script to offer (c/s/d/S/v) RDS database instance

echo -n "Use DB: "
read db

function createdb(){
	echo -n "Username: "
	read username
	echo -n "Password: "
	read password

	aws rds create-db-instance --db-instance-identifier $db --db-instance-class db.t3.micro --engine mysql --master-username $username --master-user-password $password --allocated-storage 20 | grep -wie 'DBInstanceIndentifier' -wie 'Address' | sed 's/^[ \t]*//' | sed 's/,//'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function describedb(){
	aws rds describe-db-instances --db-instance-identifier $db | grep -wie 'DBInstanceIdentifier' -wie 'DBInstanceStatus' | sed 's/^[ \t]*//' | sed 's/,//'
}

function deletedb(){
	aws rds delete-db-instance --db-instance-identifier $db --skip-final-snapshot | grep -wi 'DBInstanceStatus'
	if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}


echo -n "Command(c/d/v/x): "
read op


while [ "$op" != "x" ]
do
	case $op in
		"c")createdb
		;;
		"d")deletedb
		;;
		"v")describedb
		;;
		*)echo "Unknown Command"
		;;
	esac
	echo -n "Command(c/d/v/x): "
	read op
done














