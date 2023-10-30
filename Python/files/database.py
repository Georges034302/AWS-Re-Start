# Develop the following methods:
# - Save data to text file
# - Read data from text file
# - Save data to CSV file
# - Read data from CSV file
# - Save data to JSON file
# - Read data from JSON
import csv
import pandas
import json 

### Import this script as module for the vowels.py script

# Saving data structure (list of dictionaries) to a text file
def save_to_txt(structure):
    handler = open('data.txt','a')
    for data in structure: # data is a dictionary
        for key in data.keys(): # data.keys() returns a list of dictionary keys
            handler.write(f'{key} --> {data[key]}')
            handler.write('\n')
    handler.close()
# Reading data from file as a string structure  
def read_from_txt():
    handler = open('data.txt','r')
    structure = handler.read()
    print(structure)
    
# Saving data to a CSV file
def save_to_csv(structure):
    header = ['Vowel','Frequency']
    with open('data.csv','a') as handler:
        writer = csv.writer(handler)
        writer.writerow(header)
        for data in structure: # data is a dictionary
            for key in data.keys(): # data.keys() returns a list of dictionary keys
                writer.writerow([key,data[key]])
    # df = pandas.DataFrame(structure, columns=['Vowel','Frequency'])
    # df.to_csv('data.csv')      
          
# Reading data structure from csv file using pandas
def read_from_csv():
    structure = pandas.read_csv('data.csv')
    print(structure)
    
# Saving data structure to JSON
def save_to_json(strucutre):
    with open('data.json','w') as handler:
        json.dump(strucutre,handler,indent=2)

# Reading data string from JSON and convert to JSON
def read_from_json():
    handler = open('data.json','r')
    json_obj = json.load(handler)
    print(json.dumps(json_obj,indent=4))
    handler.close()
    