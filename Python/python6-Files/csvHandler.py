# Define a function to read from csv file
# Define a function to write to a csv file
# Each row is formatted as: 
# [student-ID, student-name, mark, grade]
# student-ID should be auto-genrated size 6-digits
# The grade should be calculated based on the mark

import csv 
import random as ran
import pandas as pd

def ids(first,last):
    return ran.sample(range(first,last),1)

def grade(mark):
    if mark >= 85:
        grade = "HD"
    elif mark >= 75:
        grade ="D"
    elif mark >= 65:
        grade = "C"
    elif mark >= 50:
        grade = "P"
    else:
        grade = "Z"
    return grade

# read method 1: using csv module
def read_from_csv(file):
    with open(file,'r') as handler:
        csv_object = csv.reader(handler)
        for row in csv_object:
            print(row)
# write method 1 using csv module                    
def write_to_csv(file,id,name,mark,grade):
    with open(file,'a',newline='') as handler:
        csv_writer = csv.writer(handler)
        row = [id,name,mark,grade]
        csv_writer.writerow(row)
        
# read method 2 using pandas
def read_pandas(file):
    header=['ID','Name','Mark','Grade']
    data = pd.read_csv(file, names=header)
    print(data)
    
def run():
    read_from_csv("students.csv")
    name = input("Name: ")
    mark = int(input("Mark: "))
    id = ids(100000,999999)[0]
    g = grade(mark)
    write_to_csv("students.csv",id,name,mark,g)
    # read_pandas("students.csv")
run()