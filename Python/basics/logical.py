x = 2
y = 5

b = x < y
print(b)

b = x <= y
print(b)

b = x > y 
print(b)

b = x >= (y-3)
print(b)

b = x == y 
print(b)

b = x != y
print(b)

b = x is y 
print(b)

b = x is not y 
print(b)

b = not(x is y)
print(b)

b = not(x == y)
print(b)

b = (not(x) or y) and (x != y) # True and True ---> True
print(b)

b = (not(x) or y) and (x == y) # True and False ---> False
print(b)

b = (x < y) or (x == y) # True or False ---> True
print(b)

b = (x > y) or (x == y) # False or False ---> False
print(b)


















