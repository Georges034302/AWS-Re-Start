import random as ran
import sys 
import statistics as stat 

# Req: generate a random list between first and last of size n
#   - first, last, n are arguments
#   - calculate the max, min, sum, average of the list

first  = int(sys.argv[1])
last = int(sys.argv[2])
n = int(sys.argv[3])
numbers = ran.sample(range(first,last),n)

print(numbers)

total = sum(numbers)    # sum built-in function calculates the total
maxx = max(numbers)     # max function returns the biggest value
minn = min(numbers)     # min function returns the smallest values
average = total/len(numbers)
meann = stat.mean(numbers)
stdv = stat.stdev(numbers)
print(f'Total = {total}')
print(f'Min = {minn}')
print(f'Max = {maxx}')
print(f'Average = {average:.2f}')
print(f'Mean = {meann:.2f}')
print(f'STDV = {stdv:.3f}')
