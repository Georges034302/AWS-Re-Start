#!/bin/bash

read -p "Delete bucket: " bucket

aws s3 rm s3://$bucket --recursive # remove the bucket content

aws s3 rb s3://$bucket

aws s3 ls