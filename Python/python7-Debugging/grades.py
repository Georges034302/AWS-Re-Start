# Read a student name from STDIN
# Given a student mark from argument
# Determine and show the grade

import sys
import pdb  # import pdb to enable Python Debugger Mode in CLI

# To start the debugger, type the following command in CLI:
# python -m pdb grades.py <integer argument>
# s     ---> step into a line and execute
# n     ---> move to next line
# exit  ---> exit the debugger

name = input("Name: ")
mark = int(sys.argv[1])

if mark >= 85:
    grade = "HD"
elif mark >= 75:
    grade ="D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "P"
else:
    grade = "Z"

print(f'{name} mark is {mark} and grade is {grade}')
