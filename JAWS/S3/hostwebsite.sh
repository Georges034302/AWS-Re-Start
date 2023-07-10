
bucket=mompopcafebackery-v$RANDOM

aws s3api create-bucket \
    --bucket $bucket \
    --region ap-southeast-2 \
    --create-bucket-configuration LocationConstraint=ap-southeast-2

aws s3api put-public-access-block \
    --bucket $bucket \
    --public-access-block-configuration "BlockPublicPolicy=false"

aws s3api put-bucket-policy --bucket $bucket --policy '{
  "Id": "Policy1688952632567",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1688952629774",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::'$bucket'/*",
      "Principal": "*"
    }
  ]
}'

aws s3 website s3://$bucket --index-document index.html

aws s3 sync MomPopCafe s3://$bucket

aws s3 ls

start http://$bucket.s3-website-ap-southeast-2.amazonaws.com
