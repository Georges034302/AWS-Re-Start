#!/bin/bash

bucket=demo-v$RANDOM  #bucket with random version number

aws s3api create-bucket \
    --bucket $bucket \
    --region ap-southeast-2 \
    --create-bucket-configuration LocationConstraint=ap-southeast-2

aws s3api put-public-access-block --bucket $bucket --public-access-block-configuration "BlockPublicPolicy=false"

aws s3api put-bucket-policy --bucket $bucket --policy '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::'${bucket}'/*"
            ]
        }
    ]
}'

aws s3 website s3://$bucket/ --index-document index.html

# aws s3 cp index.html s3://$bucket/
aws s3 sync MomPopCafe s3://$bucket

aws s3 ls 

start http://$bucket.s3-website-ap-southeast-2.amazonaws.com

