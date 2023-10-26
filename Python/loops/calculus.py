# Req: Read a value until -1
#   - determine the max values
#   - determine the min value
#   - determine the even-sum
#   - determine the even-average
import sys 

value = int(input('value = '))

total = 0
count = 0
maxx = -sys.maxsize
minn = sys.maxsize

while value != -1:
    if value > maxx:
        maxx = value
    if value < minn:
        minn = value   
    if value%2 == 0:
        total += value
        count +=1
    value = int(input('value = '))

print(f'MAX = {maxx}') 
print(f'MIN = {minn}')
print(f'TOTAL = {total}')
print(f'AVERAGE = {total/count:.2f}')