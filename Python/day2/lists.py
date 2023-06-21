# List is a collection of data of any type
# List is ordered
# List is indexed
# List allows duplicates
# List is mutable (changeable)
# Syntax: list_name = [item-0, item-1, ..., item-n]

mylist = ["Tom",34,12.5,True]

length = len(mylist)    # returns how many items in the list
print("length = "+str(length))
print(mylist)           # print the list as a string

print("First = "+mylist[0]) 
print("Last = "+str(mylist[length-1]))
print(mylist[1:3])      # slice a sublist from 1 to 2 (3 is excluded)

mylist.append("$")      # adds a value at the end of a list
print(mylist)

mylist.insert(2,"has")
print(mylist)

other_list = ['bank','AU']
total = mylist + other_list
print(total)

total.pop()     # remove the last item
print(total)

total.pop(1)
print(total)

total.remove("$")
print(total)

total.clear()   # delete all items from the list
print(total)

del total       # deletes the object

try:
    print(total)
except NameError:
    print("list does not exist")
    
del mylist[2]   # deletes item at position 2
print(mylist)

