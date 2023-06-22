# Generate a random list with:
# start from STDIN
# finish from STDIN
# n os the sample size of random values
# Show the sum, min, max values of the list

import random as ran

start = int(input("Start = "))
finish = int(input("Finish = "))
n = int(input("Size = "))

numbers = ran.sample(range(start,finish+1),n) # select n random values from range
print(numbers)

print(f'Total = {sum(numbers)}')
print(f'Max = {max(numbers)}')
print(f'Min = {min(numbers)}')