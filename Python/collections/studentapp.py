#Req: Develop a student application as follows:
#   - Register 3 students with random 3-digits ID 
#   - Each student name is read from STDIN
#   - Show the student data structure
import pprint as pp
import random as r


keys = r.sample(range(100,1000),3) # list of 3 keys
students = []
for key in keys:
    student = {}
    student['ID'] = key
    student['name'] = input('Name: ')
    students.append(student)
    
pp.pprint(students,indent=2,width=20)
