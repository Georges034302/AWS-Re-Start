#Req: add all the elements in a range
#   - first is from STDIN
#   - last is from STDIN
#   - show the total

first = int(input('first = '))
last = int(input('last = '))

total = 0
for e in range(first,last+1):
    total += e 

print(f'TOTAL = {total}')