# Dictionary is a collection of data of any type
# Dictionary data is formatted as entries: key-value
# Dictionary is unordered
# Dictionary is not indexed
# Dictionary keys are unique, values can be duplicated 
# Dictionary is mutable (changeable)
# Syntax: dictionary_name = {
                        # key0:item-0, 
                        # key1:item-1, 
                        # ..., 
                        # key-n:item-n}
import pprint as pp
                    
mydata = {
    "name":"Tom",
    "age":35,
    "role":"admin",
    "active": True
}

print(mydata)
print()
pp.pprint(mydata,width=40)

mydata['age'] = 45
pp.pprint(mydata,width=40)

del mydata["active"]
pp.pprint(mydata,width=40)

del mydata

try:
    print(mydata)
except NameError:
    print("dictionary does not exist")