# Read a string from STDIN
# print the string characters separated by comma on the same line
# count and show the number of white spaces

s = input("String: ")

for c in s:
    print(c, end=", ")
print()

# Method 1
count = 0
i = 0

while i < len(s):
    if s[i] == ' ':
        count+=1
    i+=1
print("s has: "+str(count)+" spaces")

# Method 2
print(f's has {s.count(" ")}')
