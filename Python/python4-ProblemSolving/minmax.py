# Read a value from STDIN until -1
# Determine the max value
# Determine the min value
# Show the min and max
import sys

n = int(input("n = "))

# Method 1
minimum = sys.maxsize # 2**63
maximum = -sys.maxsize
total = 0
count = 0
while n != -1:
    if n < minimum:
        minimum = n
    if n > maximum:
        maximum = n
    total += n 
    count +=1 
    n = int(input("n = "))
    
print(f'Min = {minimum}')
print(f'Max = {maximum}')
print(f'Total = {total}')
print(f'Average = {total/count:.2f}')

# Method 2
# numbers = []
# while n != -1:
#     numbers.append(n)
#     n = int(input("n = "))

# print(f'Min = {min(numbers)}')
# print(f'Max = {max(numbers)}') 
# print(f'Total = {sum(numbers)}')   
# print(f'Average = {sum(numbers)/len(numbers):.3f}') 