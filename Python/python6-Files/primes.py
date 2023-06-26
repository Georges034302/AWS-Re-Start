# Select a random sample from a range (first,last) 
# sample size is read from STDIN
# first and last are read from STDIN
# Show the random list
# Determine and show the prime numbers from that list
### Save the primes to a txt file
### Read all primes from txt file and calculate the total

import random as ran

def random_list(first,last,howmany):
    return ran.sample(range(first,last),howmany)

def is_prime(n):
    for e in range(2,n):
        if n % e == 0:
            return False
    return True

def primes_list(numbers):
    primes = []
    for e in numbers:
        if is_prime(e):
            primes.append(e)
    return primes

def save_to_txt_file(primelist):
    fileHandler = open("primes.txt","a")
    fileHandler.write(str(primelist))
    fileHandler.write("\n")
    fileHandler.close()
    
def read_from_txt_file():
    fileHandler = open("primes.txt","r")
    content = fileHandler.read()
    print(content)
    fileHandler.close()
    
def total_primes():
    fileHandler = open("primes.txt","r")
    content = fileHandler.readlines()
    
    total = 0
    for line in content: # line here is a string-list
        total += sum(eval(line)) # eval convert string-list to list
    fileHandler.close()
    return total
    
def run():
    first = int(input("First = "))
    last = int(input("Last = "))
    size = int(input("Size = "))
    mylist = random_list(first,last,size)
    #print(mylist)
    primes = primes_list(mylist)
    #print(primes)
    print("Backing up primes to file ...")
    save_to_txt_file(primes)
    print("Reading all primes ...")
    read_from_txt_file()
    print(f'Total primes = {total_primes()}')
run()