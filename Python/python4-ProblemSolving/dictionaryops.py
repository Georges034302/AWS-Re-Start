# Create a dictionary with random 3-digit IDs (as keys)
# Size of the IDs (how many) is enter from STDIN
# Associate the IDs with names from STDIN
# Show the dictionary (as JSON like document)
# Show the sorted dictionary by IDs

import random as ran
import pprint as pp

howmany = int(input(" Keys size = "))
keys = ran.sample(range(100,1000),howmany)
print(keys)

names = {}
for key in keys:
    names[key] = input("Name: ")
pp.pprint(names, width=30)

for key in sorted(names.keys()):
    print("%s - %s"%(key,names[key]))
    
    