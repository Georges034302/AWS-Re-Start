import json
import random as ran

def ran_ids(first,last,n):
    return ran.sample(range(first,last),n)

def lambda_handler(event, context):
    ids = ran_ids(100000,1000000,4) # generate 4 ids of size 6-digits
    names = ['Tom Jones','Lana Smith','Alex Lin','Jane Doe']
    roles = ['Admin','Hr','Developer','Architect']
    
    employees = {}
    
    i = 0
    while i < len(ids):
        employees[ids[i]] = {} # Identify id as primary key
        employees[ids[i]]['name'] = names[i]
        employees[ids[i]]['role'] = roles[i]
        i += 1
        
    return {
        'statusCode': 200,
        'body': employees # JSON --> dictionary containing multiple dictionaries
    }
