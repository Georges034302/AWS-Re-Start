# Read a string until * is entered
# Map the vowels and their frequencies to a dictionary
# Show the dictionary as JSON format

import pprint as pp 

# Step 1: This function returns the count of c in a string
def frequency(c, string):
    return string.lower().count(c)

# Step 2: Map the frequencies of vowels in a string to a dictionary
def frequencies(string):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,string)
    return data

def show(data):
    pp.pprint(data,indent=2, width=20)
    
def run():
    s = input("String: ")
    while s != "*":
        show(frequencies(s))
        s = input("String: ")
run()
        