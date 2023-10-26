#Req: Read values from STDIN until -1
#   show the total of all values

value = int(input('value = '))

total = 0
while value != -1:
    total += value
    value = int(input('value = '))
    
print(f'TOTAL = {total}')