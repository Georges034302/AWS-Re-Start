# There are two types of methods in Python
#
# 1 - Procedures:
#   - Procedures are methods that do not return a value
#   - Procedures are methods do an action (i.e. move, jump, eat, dive, ...)
#   - Procedures are named as verbs
#   - Syntax:
#       def <verb>(parameters):
#           <action(s)>

def move(distance):
    pos = 0 # local varibales must always be initialized
    pos += distance
    print(f"current position = {pos}")
move(20)    # a procedure is called like a command

#
# 2 - Functions:
#   - Functions are methods that return a value
#   - Functions are methods solve expression(s) 
#   - Functions are named as nouns (i.e. area, customer, product, ...)
#   - Syntax:
#       def <noun>(parameters):
#           <solve expression(s)>
#           return <value(s)>
def distance(speed,time):
    return speed*time 

# Function is always called like a value
print(f"Travelled distance = {distance(40,5)} KM")

# NOTE: 
# - parameter is a variable (placeholder) given to the method at definition phase
# - argument is a value given to the method and injected in the place of parameter when the method is invoked (called)
# - global variables must be label 'global' in a method