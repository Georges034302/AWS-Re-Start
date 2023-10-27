# Req: Determine and show the prime list from a random list
#   - generate a random list of integers from start to finish of size n
#   - determine if a number is a prime number
#   - determine the primes from the random list
#   - show both lists
#   - define a CLI menu system to offer (g/p/s/x)
#   (g) generate a random list
#   (p) determine prime list
#   (s) show both lists
#   (x) exit

import random as ran 

# returns a list of n-randoms
def numbers(start,finish,n):
    return ran.sample(range(start,finish+1),n)

# check if a number n is prime using the any-pattern
def is_prime(n):
    for e in range(2,n):
        if n % e == 0:
            return False
    return True

# finding every prime in a list using the every-pattern
def primes(mylist):
    prime_list = []
    for e in mylist:
        if is_prime(e):
            prime_list.append(e)
    return prime_list

# show many arguments
def show(*args):
    print(*args)

def run():
    choice = input('Command(g/p/s/x): ')
    values = []
    prime_list = []
    while choice != 'x':
        match choice:
            case 'g': values = numbers(int(input('start = ')),int(input('finish =')),int(input('n =')))
            case 'p': prime_list = primes(values)
            case 's': show(values), show(prime_list)   
            case _: print('Unknown command')
        choice = input('Command(g/p/s/x): ')
run()