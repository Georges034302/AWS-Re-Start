# Create a dictionary of students with random 3-digit IDs (as keys)
# Size of the IDs (how many) is enter from STDIN
# Associate the IDs with names from STDIN
# Show the sorted dictionary by IDs
# update a dictionary entry by key 
# delete a dictionary entry by key
# add entries to dictionary
# Use functions to reformat the code
# NOTE: read the required values from STDIN


import random as ran
import pprint as pp

def ids(first,last,size):
    return ran.sample(range(first,last),size)

def students(keys):
    names = {}
    for key in keys:
        names[key] = input("Name: ")
    return names

def show_sorted(names):
    for key in sorted(names.keys()):
        print("%s - %s"%(key,names[key]))
        
# Use the any pattern to check if a key exists  
def exist(names, key):
    for id in names.keys():
        if id == key:
            return True
    return False
     
def update(names,key,value):    
    if exist(names,key):
         names[key] = value
    else:
        print(f"Student with key: {key} does not exist")

def delete(names,key):   
    if exist(names,key):
        del names[key]
    else:
        print(f"Student with key: {key} does not exist")
            
def add(names, key, value):
    if not(exist(names,key)):
        names[key] = value
    else:
        print(f"Student with key: {key} already exists")
            
def run():
    size = int(input("Size = "))
    keys = ids(100,1000,size)
    names = students(keys)
    show_sorted(names)
    key = int(input("Update by key = "))
    value = input("Update with value = ")
    update(names,key,value)
    key = int(input("Delete by key = "))
    delete(names,key)
    key = int(input("Add key = "))
    value = input("Add value = ")
    add(names,key,value)
    show_sorted(names)
run()
    