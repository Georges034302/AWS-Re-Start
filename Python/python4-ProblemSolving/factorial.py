# Read a value from STDIN until -1
# Calculate and show the factorial of each value

import math as m 

n = int(input("n = "))

#Method 1
while n != -1:
    print(f'Factorial({n}) = {m.factorial(n)}')
    n = int(input("n = "))

# Method 2
# while n != -1:
#     f = 1
#     for e in range(1,n+1):
#         f*= e 
#     print(f'Factorial({n}) = {f}')
#     n = int(input("n = "))
# print("done")