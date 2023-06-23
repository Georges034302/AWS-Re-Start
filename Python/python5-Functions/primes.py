# Select a random sample from a range (first,last) 
# sample size is read from STDIN
# first and last are read from STDIN
# Show the random list
# Determine and show the prime numbers from that list

import random as ran

def random_list(first,last,howmany):
    return ran.sample(range(first,last),howmany)

# Step 1: verify if a number is prime
# Use the none-pattern:
# for <value> in <range>:
#   if <condition>:
#       return False
# return True

def is_prime(n):
    for e in range(2,n):
        if n % e == 0:
            return False
    return True
# Use the every pattern to create a lookup function to match primes and return a list of primes
# for <value> in <range>:
#   if not(<condition>):
#       return False
# return True
def primes_list(numbers):
    primes = []
    for e in numbers:
        if is_prime(e):
            primes.append(e)
    return primes

def run():
    first = int(input("First = "))
    last = int(input("Last = "))
    size = int(input("Size = "))
    mylist = random_list(first,last,size)
    print(mylist)
    print(primes_list(mylist))
run()