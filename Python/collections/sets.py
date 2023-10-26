# Set is a collection of any data type
# Set is unordered
# Set is not indexed
# Set is changeable
# Set does not allow duplicates (only unique items)
# Syntax: set_name = {item, other-item, ... , more-item}

myset = {'AWS',2023,'restart',13,'python'}
print(myset)

# Cannot access items by index, since set is not indexed

# Adding to set
myset.add('java')
print(myset)

# Deleting from set
myset.remove(13)        # delete item by name
print(myset)

myset.discard('java')   # delete item by name
print(myset)

myset.pop()             # randomly delete an item
print(myset)

# Join 2 sets
other_set = {'java','C#'}

total_set = myset.union(other_set)
print(total_set)