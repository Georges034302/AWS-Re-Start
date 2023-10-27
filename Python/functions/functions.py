# Method is a block of code with a name
# Method is reusable
# Method is called by name anywhere in the program

# Method in python is a function or procedure:

#   - Function is a method that returns a value
#   - Function is always a noun
#   - Function returned-value can be stored into a variable
#
#   * Syntax:
#       def noun(args):
#           return <value>
# Example:
import math as m 

def area(radius):
    return m.pi*pow(radius,2)

a = area(2) # function returned value is stored into variable a
print(a)

#   - Procedure is a method that does an action and return nothing
#   - Procedure is always a verb
#   - Procedure cannot be stored into a variable
#
#   * Syntax:
#       def verb(args):
#           <action>
# Example:
def show(name):
    print('My name is '+name)
    
show('Tom') # procedure is only displaying String to STDOUT