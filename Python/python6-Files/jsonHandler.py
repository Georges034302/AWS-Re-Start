# Read csv data from students.csv
# Write the data to JSON file formatted as dictionaries
# Read data from JSON file as dictionary format
import csv 
import json 

def read_from_csv(file):
    data = []
    with open(file,'r') as handler:
        csv_object = csv.DictReader(handler)
        for row in csv_object:
            data.append(row)
        handler.close()
    return data      

def save_to_json(file, data):
    handler = open(file,'w+')
    handler.write(json.dumps(data,indent=4))
    handler.close()
    
def run():
    data = read_from_csv("students.csv")
    save_to_json("students.json",data)
    
run()