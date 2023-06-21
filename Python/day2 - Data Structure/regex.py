
# \ escape
# ? means 0 or 1 of previous character
# * means 0 or many of previous character
# + means 1 or many of the previous character
# \d means 1 digit similar to [0-9]
# ^ indicates beginning of a line
# $ indicates end of a line
# \s indicates white space
# {m,n} quantifier from m to n quantity
# [a-z] lower-case character
# [A-Z] upper-case character
# [] allows select of one enclosed character

txt ="""
^Python3.10 is fun
1 -we learned lists
2 -we learned strings 
3 -Python has 100 functions
Date: 21/06/2023
"""
import re  

obj = re.search("\d",txt)
print(obj)

obj = re.search("\d{2}",txt)
print(obj)

obj = re.findall("\d{2}",txt) # find all 2 digits and return a list of findings, similar to grep
print(obj)

new_text = re.sub("python", "JAVA",txt, flags=re.IGNORECASE) # similar to sed in bash
print(new_text)



