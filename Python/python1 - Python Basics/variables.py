# declaring variables
a = 5 # this makes a an integer type
b = 2 # b is now integer
f = 3.5 # this makes a a floating type
s = "Hello" # s is a string
b = True # b is changed to boolean
c = 1+2j # c is a complex number

print(type(a)) # function type tells the type of value stored
print(type(b))
print(type(f))
print(type(s))
print(type(c))

print(a+f)
print(a+b)
print(str(a)+" "+s)
print(str(b)+" " + s)

x = a + 2
print(x)

x += a  # x = x + a
print(x)

x -= 3 # x = x - 3
print(x)

x /= 3 # x = x/3
print(x)

x %= 2 # x = x%2
print(x)

x = 2 * 3 + 1
print(x)
x = 2 * (3 + 1) # DODMAS
print(x)