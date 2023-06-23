# Read in a number until -1 between 0 and 999 from STDIN
# Convert this number to words
# Example:
# Number: 0
# Word: zero
#
# Number: 18
# Word: eighteen
#
# Number: 121
# Word: one hundred and one
#
# Number: 200
# Word: two hundred
# Recommended approach: Incremental goals

def word(number):
    numNames = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
    tensNames = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # number ---> abc
    rest = number%100           # bc
    ones = rest%10              # c
    tens = int(rest/10)         # b
    hundreds = int(number/100)  # a
    
    word = ""
    
    if hundreds > 0:
        word += numNames[hundreds] + " hundred "
    if hundreds > 0 and rest > 0:
        word += " and "
    if tens >= 2:
        word += tensNames[tens]+" "+numNames[ones]
    elif number == 0:
        word="zero"
    else:
        word += numNames[rest]
    return word

def show_word():
    number = int(input("Number: "))    
    while number != -1:
        print(f"Word: {word(number)}")
        number = int(input("Number: "))
        
show_word()
        