# Define a function to divide two numbers
# Handle the division by zero exception
# Exception is a runtime error caused by an expression
# Exception can be prevented (not allowed to happen)
# Exception can be caught and handled (allowed to happen)

def div(a,b):
    return a/b

# Method 1: prevent the exception
a = int(input("a = "))
b = int(input("b = "))
while b == 0:
    print("b is zero, this can cause division by zero error")
    b = int(input("Try again. b = "))
print(div(a,b))

# Method 2: handle the exception
a = int(input("a = "))
b = int(input("b = "))
try:
    print(div(a,b))
except ZeroDivisionError: 
     print("b is zero, this can cause division by zero error")
print("Division did not occur!!!")
