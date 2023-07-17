import json
import boto3
import ast

def lambda_handler(event, context):
    
    s3_client = boto3.client('s3')                  # connect to the s3 service
    dynamodb_client = boto3.resource('dynamodb')    # connect to the dynamodb service

    bucket = event['Records'][0]['s3']['bucket']['name']   # fetch first bucket by name
    json_file = event['Records'][0]['s3']['object']['key'] # fetch first record in the bucket by key
    
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file) # create a json object
    file_reader = json_object['Body'].read().decode("utf-8")        # read the json content
    file_reader = ast.literal_eval(file_reader)                     # convert the content to a list of dictionaries
    
    table = dynamodb_client.Table('studentstable')                  # create a dynamodb table instance
    
    for d in file_reader:                           # read each dictionary from the json
        table.put_item(Item=d)                      # save every dictionary to the dynamodb table
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Successful JSON mapping')
    }
