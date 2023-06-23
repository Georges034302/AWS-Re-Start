# Read an integer n from STDIN
# Calculate the quadratic value of n+2  ---> (n+2)^2 = n^2 + 2*n*2 + n^2
# Calculate the sum series from 1 until n
# Calculate and show the factorial series of n
# Define the main method to execute all above methods
import math as m 

def quadratic(n):
    return pow(n,2) + 2*n*2 + pow(2,2)

def sum_series(n):
    return sum(range(1,n+1))

def show_factorial_series(n):
    for e in range(1,n+1):
        print(f'{n:3} --> {m.factorial(e):4}')
        
def run():
    n = int(input("n = "))
    print(f'Quadratic({n}) = {quadratic(n)}')
    print(f'Sum Series of ({n}) = {sum_series(n)}')
    show_factorial_series(n)
    
run()
