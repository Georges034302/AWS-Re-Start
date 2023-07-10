echo -n "Remove bucket: "
read bucket

aws s3 rm s3://$bucket --recursive #empty the bucket

aws s3 rb s3://$bucket 

aws s3 ls