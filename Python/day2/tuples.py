# Tuple is a collection of data of any type
# Tuple is ordered
# Tuple is indexed
# Tuple allows duplicates 
# Tuple is immutable (none changeable)
# Syntax: tuple_name = (item-0, item-1, ..., item-n)

mytuple = ("Tom",30,12.45) # immutable items are fixed

print(mytuple)

length = len(mytuple)

print(mytuple[0])

other_tuple = ("Bank","AU")

total = mytuple + other_tuple
print(total)

del total

try:
    print(total)
except NameError:
    print("tuple does not exist")