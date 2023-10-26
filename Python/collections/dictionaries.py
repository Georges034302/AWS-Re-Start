# Dictionary is a collection of data of any type
# Dictionary items are formatted as key:value
# Dictionary is unordered
# Dictionary is not indexed
# Dictionary keys are unique, values can be duplicated
# Dictionary is changeable (mutable)
# Syntax: data = {
#                   'key-0':'value-0',
#                   .....
#                   'key-n':'value-n'
#               }
import pprint as pp

employee = {
        'name':'Alex',
        'age': 45,
        'role':'admin'
        }

print(employee)
pp.pprint(employee,indent=2,width=40)

# Access/Read items
print(employee['age'])

# Add items
employee['salary'] = 100000
pp.pprint(employee,indent=2,width=40)

# Update items
employee['name'] = 'Jason Smith'
pp.pprint(employee,indent=2,width=40)

# Delete items
del employee['age']
pp.pprint(employee,indent=2,width=40)
