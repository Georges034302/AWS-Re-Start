s = "AWS Restart MAY2023"

length = len(s)

print("Length of s = ",length)

# access string characters by index: s[index]
print(s[0])
print(s[length-1])
print(s[int((length-1)/2)]) # int() casts a float to int
print(s[2:6]) # s[first:last] returns a slice of the string until last -1
print(s[5:]) # slice from 5 until the end of the string

print(s.count('a')) # count how many 'a'
print(s.lower().count('a'))

print(s.upper())
print(s.replace("AWS","Python"))
print(s.index('M'))
print(s.index('A'))
print(s.find('M'))

print(s.isalpha())
print(s.isnumeric())
print(s.isalnum())