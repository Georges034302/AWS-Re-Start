
import sys 

print(sys.argv[0]) # similar to $0 in BASH

x = int(sys.argv[1]) # first argument given to the script
y = int(sys.argv[2]) # second argument given to the script

print(x**y) # x power y

# read values from STDIN
x = int(input("x = "))
print(x + 2)

name = input("Name: ")
print("welcome ",name)