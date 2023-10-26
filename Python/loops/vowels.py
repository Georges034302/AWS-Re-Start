#Req: Read a string from STDIN until *
# Determine and show the vowels frequencies 
# Format the output as:
#   vowel --> frequency

s = input('string: ')

while s != '*':
    for c in 'aeiou':
        frequency = s.lower().count(c)
        print(f'{c} --> {frequency}')
    s = input('string: ')
