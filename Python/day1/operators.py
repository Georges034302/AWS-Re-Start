x = 2
y = 3

print(x is y) 
print(x == y)

print(x is not y)
print(not(x is y))
print(x != y)
print(not(x == y))

print(x >= y)
print(x < y)

b = (not(x) and (y>x)) or (x+3 > 4) 
print(b)

b = (x < y or x > y) and (y+1 > 3)
print(b)
