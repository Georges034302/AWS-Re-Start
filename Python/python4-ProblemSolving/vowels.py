# Read a string from STDIN until *
# Determine the frequency of each vowel in the string
# Determine the total number of vowels in the string
# Show the values 

s = input("String: ")

while s != "*":
    total = 0 
    
    for c in "aieou":
        frequency = s.lower().count(c)
        total += frequency
        print(f'{c:2} --> {frequency:2}')
    print(f"Vowel count = {total}")
    s = input("String: ")
    
print("Thank you")