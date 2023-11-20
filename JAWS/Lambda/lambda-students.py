import json
import boto3
import ast

def lambda_handler(event, context):
    s3_client = boto3.client('s3') # connect to the s3 service
    dynamodb_client = boto3.resource('dynamodb') # connect to the dynamodb service
    bucket = event['Records'][0]['s3']['bucket']['name'] # getting the bucket name 
    file_name = event['Records'][0]['s3']['object']['key'] # get the file name from the bucket
    json_object = s3_client.get_object(Bucket=bucket,Key=file_name) # Load the file content into JSON object
    file_reader = json_object['Body'].read().decode("utf-8") # Load Json data from object
    file_reader = ast.literal_eval(file_reader) # convert the JSON data to literals
    table = dynamodb_client.Table('students-table') # getting the dynamodb table object
    
    for data in file_reader:
        table.put_item(Item=data) # Save every dictionary object int the jason file to the table
    
    return {
        'statusCode': 200,
        'body': json.dumps('Students JSON saved successfully to dynamodb')
    }
