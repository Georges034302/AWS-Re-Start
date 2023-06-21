# Set is a collection of data of any type
# Set is unordered
# Set is not indexed
# Set does not allow duplicates (items are unique)
# Set is mutable (changeable)
# Syntax: set_name = {item-0, item-1, ..., item-n}

set1 = {"AWS",2023,"restart","AU",11}
print(set1)

set1.add("AWS") # AWS is not added, duplicate items are not allowed
print(set1)

set1.update(["June",21]) # add a list items to a set
print(set1)

set1.remove("June")     # remove item
print(set1)

set1.discard(11)        # remove item 
print(set1)

set2 = {"Cohort", 15}
myset = set1.union(set2)    # join two sets
print(myset)

myset.pop()     # randomly remove an element
print(myset)

del set1
try:
    print(set1)
except NameError:
    print("set does not exist")

