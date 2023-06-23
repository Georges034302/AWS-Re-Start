# Select a random sample from a range (first,last) 
# sample size is read from STDIN
# first and last are read from STDIN
# calculate the statistic values: min, max, total, mean, stdv, variance
# Show the calculated values

import random as ran
import statistics as stat 

def random_list(first,last,howmany):
    return ran.sample(range(first,last),howmany)

def values(*argv):
    minimum = min(*argv)
    maximum = max(*argv)
    total = sum(*argv)
    return minimum, maximum, total 

def stat_values(*argv):
    m = stat.mean(*argv)
    stdv = stat.stdev(*argv)
    v = stat.variance(*argv)
    return m, stdv, v

def run():
    first = int(input("First = "))
    last = int(input("Last = "))
    size = int(input("Size = "))
    mylist = random_list(first,last,size)
    minimum, maximum, total = values(mylist)
    m, stdv, v = stat_values(mylist)
    print(f"Max = {maximum}")
    print(f"Min = {minimum}")
    print(f"Total = {total}")
    print(f"Mean = {m}")
    print(f"STDV = {stdv:.2f}")
    print(f"Variance = {v:.3f}")
    
run()