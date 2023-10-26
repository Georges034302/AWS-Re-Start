# List is a collection of any data types
# List is ordered
# List is indexed
# List is changeable --> CRUD
# List allows duplicates
# Syntax: list_name = [item-0,item-1, ... , item-n]

mylist = ['Tom',34,12.55,True]

print(len(mylist))              # size of a list

# Reading from list
print(mylist[0])                # first item
print(mylist[len(mylist)-1])    # last item
print(mylist[1:3])              # gets item 1 and item 2

# Creating/Adding items
mylist.append('balance')        # Add item to the end of the list
print(mylist)   

mylist.insert(2,'$')            # Add item at a position in the list
print(mylist)

other_list = ['bank','AU']
total = mylist + other_list     # Joining 2 lists
# print(total)

# Updating items
mylist[0] = 'Jason'
print(mylist)

# Delete items
mylist.pop()                    # Removes the last item
print(mylist)

mylist.pop(2)                   # Removes item 2
print(mylist)

mylist.remove('Jason')          # Remove object by name
print(mylist)

del mylist[1]                   # Removes item 1
print(mylist)


mylist.clear()                  # Delete all items
print(mylist)

del mylist                      # Delete the mylist object
try:
    print(mylist)
except NameError:
    print('mylist does not exist')
    