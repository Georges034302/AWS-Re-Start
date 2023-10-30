#Req: Read a string from STDIN until *
# Determine and show the vowels frequencies 
# Format the output as:
#   vowel --> frequency
# Store the result in a dictionary
# Store the dictionaries in a list

import pprint as pp
import database as db

# determine the frequency/count of c in s
def frequency(c,s):
    return s.lower().count(c)

# determine the vowels frequency and add it to dictionary
def frequencies(s):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,s)
    return data
    
def show(data):
    pp.pprint(data,indent=2,width=20)
    print()
        
def view(structure):
    for data in structure:
        show(dict(data))
        
def run():
    s = input('string: ')
    structure = []
    while s != '*':
        structure.append(frequencies(s))
        s = input('string: ')
    db.save_to_txt(structure)
    db.save_to_csv(structure)
    db.save_to_json(structure)
    db.read_from_txt()    
    db.read_from_csv()
    db.read_from_json()
    
run()