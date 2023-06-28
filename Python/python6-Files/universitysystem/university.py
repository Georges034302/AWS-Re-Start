#This main-script should offer admins (CRUD-V) options to:
# Add a student to CSV (C)
# Read a student from CSV (R)
# Update student mark in CSV (U)
# Delete a student from CSV (D)
# Read all students from CSV (V)
#main-script offers system menu to admins to perform CRUD-V operations
import students as s 

FILE = 'students.csv'

def create():
    id = int(input("ID: "))
    name = input("Name: ")
    mark = int(input("Mark: "))
    s.add_student(FILE,id,name,mark)
    print(f'{name} record has been created \n')
    
def read():
    id = int(input("ID: "))
    row = s.student(FILE,id)
    if len(row) > 0:
        print("Student record: "+str(row)+"\n")
    else:
        print("Student record does not exist!")
        
def update():
    id = int(input("ID: "))
    mark = int(input("Mark: "))
    row = s.student(FILE,id)
    if len(row) > 0:
        s.update_student(FILE,id,mark)
        print("Student record has been updated successfully\n")
    else:
        print("Student record does not exist!")

def delete():
    id = int(input("ID: "))
    row = s.student(FILE,id)
    if len(row) > 0:
        s.delete_student(FILE,id)
        print("Student record has been deleted successfully\n")
    else:
        print("Student record does not exist!")
     
def view():
    data = s.students(FILE)
    for row in data:
        print(row)
    
#system menu options should be actions without arguments
def switch(choice):
    if choice == "c":
        create()
    elif choice == "r":
        read()
    elif choice == "u":
        update()
    elif choice == "d":
        delete()
    elif choice == "v":
        view()
    else:
        print("Unknown Command!")

def run():
    choice = input("Command(c/r/u/d/v/x): ")
    while choice != "x":
        switch(choice)
        choice = input("Command(c/r/u/d/v/x): ")
    print("Thank you!")
run()