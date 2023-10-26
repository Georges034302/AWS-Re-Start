#Req: Determine the factorial of n (from STDIN) until -1 (Factorial series)
# n! = n*(n-1)*...*2*1

n = int(input('n = '))

while n != -1:    
    f = 1
    for e in range(1,n+1):
        f *= e 
    print(f'Factorial({n}) = {f}')
    n = int(input('n = '))



# import sys 

# n = int(sys.argv[1]) # First argument given to the script

# f = 1
# for e in range(1,n+1):
#     f *= e 
# print(f'Factorial({n}) = {f}')