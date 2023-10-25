s = 'AWS restart program 2023'

length = len(s) # since len() is a function, result value is stored into a variable length
print(length)
print(len(s))

# s[index] --> returns the character at position index in the string
print(s[0])

# last character is at position length-1
print(s[length-1])

# slice between position a an b --> s[a:b+1]
print(s[2:6])
print(s[6:])

print(s.count('a'))
print(s.upper())
print(s.lower())
print(s.lower().count('a'))

print(s.index('a')) # position of first a in the string
print(s.find('2'))  # position of first 2 in the string

print(s.replace('restart','python'))

print(s.isalpha())
print(s.isalnum())
print(s.capitalize())



