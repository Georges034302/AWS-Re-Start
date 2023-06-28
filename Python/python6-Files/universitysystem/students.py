import csv
import pandas as pd

# function to return grade from mark
def grade(mark):
    if mark >= 85:
        grade = "HD"
    elif mark >= 75:
        grade = "D"
    elif mark >= 65:
        grade = "C"
    elif mark >= 50:
        grade = "P"
    else:
        grade = "Z"
    return grade
# add a new student to the CSV
def add_student(file,id,name,mark):
    with open(file,'a',newline='') as f:
        writer = csv.writer(f)
        g = grade(mark)
        row = [id,name,mark,g]
        writer.writerow(row)

# read a student from CSV by ID (any pattern)
def student(file,id):
    data = []
    with open(file,'r') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if int(row[0]) == int(id):
                data.append(row)
    return data

# read all students from CSV
def students(file):
    data = []
    with open(file,'r') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:            
            data.append(row)
    return data

# update a student mark by ID in CSV
def update_student(file,id,mark):
    df = pd.read_csv(file) #Create a data frame table
    row_num = df[df['ID'] == id].index.tolist() #find the row number of target ID
    g = grade(mark)
    row = student(file,id)
    df.loc[row_num[0],'Mark'] = mark #locate a row number and match column name
    df.loc[row_num[0],'Grade'] = g
    df.to_csv(file,index=False)
    
# delete a student by ID in CSV
def delete_student(file,id):
    df = pd.read_csv(file) #Create a data frame table
    row_num = df[df['ID'] == id].index.tolist() #find the row number of target ID
    df.drop(row_num[0],inplace=True)
    df.to_csv(file,index=False)
    

