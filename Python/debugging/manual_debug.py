import pdb 
# execute the script with: python3 -m pdb manual_debug.py

first = int(input('first = '))
last = int(input('last = '))

total = 0
for e in range(first,last+1):
    total += e 

print(f'TOTAL = {total}')