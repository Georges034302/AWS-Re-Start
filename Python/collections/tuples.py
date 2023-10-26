# Tuple is a collection of any data
# Tuple is ordered
# Tuple is indexed
# Tuple is immutable (un-changeable) - Read-Only
# Tuple allows duplicates
# Syntax: tuple_name = (item=0, item-1, ... , item-n)

mytuple = ('AWS','restart',2023,'Goanna')

print(mytuple)
print(len(mytuple))

# Access/Read items by index
print(mytuple[0])
print(mytuple[len(mytuple) - 1])

other_tuple = ('Java','JDK',17)

total = mytuple + other_tuple
print(total)

# Tuple items cannot be removed
# We cannot add more items to tuple
# We cannot update item values in a tuple

