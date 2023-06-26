# Define a system menu to use the dictionaryops functions
# The system menu should offer users the following options:
# Choice (c/r/u/d/v/x):
# c - add entry to dictionary
# r - read entry from dictionary
# u - update entry in dictionary
# d - delete entry in dictionary
# v - view all entries
# x - to exit

import dictionaryops.dictionaryops as dops

# Generate a new dictionary
def data():
    names = {}
    first = int(input("first = "))
    last = int(input("last = "))
    n = int(input("size = "))
    keys = dops.ids(first,last,n)
    names = dops.students(keys)
    return names

names = data() # data set

def create():
    key = int(input("key = "))
    value = input("value = ")
    dops.add(names,key,value)

def read():
    key = int(input("key = "))
    if dops.exist(names,key):
        print(f"{key} --> {names[key]}")
    else:
        print("No value associated with ", key)
        
def update():      
    key = int(input("key = "))
    value = input("value = ")
    dops.update(names, key, value)    
    
def delete():
    key = int(input("key = "))
    dops.delete(names,key)
    
def view():
    dops.show_sorted(names)
        
def menu():
    choice = input("Choice(c/r/u/d/v/x): ")
    while choice != "x":
        match choice:
            case 'c': create()
            case 'r': read()
            case 'u': update()
            case 'd': delete()
            case 'v': view()
            case _ : print("Unknown choice!")
        choice = input("Choice(c/r/u/d/v/x): ")
menu()
                