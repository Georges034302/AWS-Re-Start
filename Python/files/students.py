#Req: Read and show students.csv data
# Add new student to csv file:
# - student ID is random 6-digits
# - student mark is random between 25 and 100
# - student grade is auto-calculated based on the mark
# - Student is from STDIN

import csv 
import pandas as pd
import random as ran

def random_ID():
    return ran.randint(100000,999999)

def random_mark():
    return ran.randint(25,100)

def auto_grade(mark):
    if mark >= 85:
        grade = 'HD'
    elif mark >= 75:
        grade = 'D'
    elif mark >= 65:
        grade = 'C'
    elif mark >= 50:
        grade = 'P'
    else:
        grade = 'Z'
    return grade

def read_from_csv():
    with open('students.csv','r') as handler:
        reader = csv.reader(handler)
        for row in reader:
            print(row)
            
def read_from_csv_pandas():
    data = pd.read_csv('students.csv')
    print(data)
    
def add_student():
    name = input('Student name: ')
    ID = random_ID()
    mark = random_mark()
    grade = auto_grade(mark)
    row = [ID,name,mark,grade]
    
    with open('students.csv','a',newline='') as handler:
        csv_writer = csv.writer(handler)
        csv_writer.writerow(row)
        
def run():
    read_from_csv()
    add_student()
    read_from_csv_pandas()

run()