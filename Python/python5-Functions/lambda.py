# Read an integer n from STDIN
# Calculate the quadratic value of n+2  ---> (n+2)^2 = n^2 + 2*n*2 + n^2
# Calculate the sum series from 1 until n
# Calculate the factorial of n
# Define the main method to execute all above methods
# NOTE: Use lambda functions and recursion to solve the problem

def quadratic(n):
    Q = lambda n: pow(n,2) + 2*n*2 + pow(2,2)
    return Q(n)

def sum_series(n):
    S = lambda n: n + S(n-1) if n > 1 else 0
    return S(n)

def factorial(n):
    F = lambda n: n * F(n-1) if n > 1 else 1
    return F(n)

def run():
    n = int(input("n = "))
    print(f'Quadratic({n}) = {quadratic(n)}')
    print(f'Sum Series of ({n}) = {sum_series(n)}')
    print(f'Factorial({n}) = {factorial(n)}')
    
run()
