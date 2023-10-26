# Req: Read a name from STDIN
# welcome the name is they are Alana
# Otherwise say goodbye
# Get Alana bonus-value from argument
import sys 

name = input('Enter a name: ') # read strings from STDIN
salary = int(input('Enter salary: '))
bonus = int(sys.argv[1]) # argv captures arguments as strings
salary = salary + bonus

if name == 'Alana':
    print(f'Welcome {name} your bonus is {salary}')
else:
    print('Goodbye!')
    
