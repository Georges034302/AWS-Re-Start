x = 2
y = 3

z = x + y 
print(z)

x += 2 # x = x + 2
print(x)

x -= 1 # x = x - 1
print(x)

x *= 2 # x = x * 2
print(x)

try: # try clause help prevent critical code exceptions
    x = 2
    y = '3'
    z = x + y 
    print(z)
except TypeError:
    y = 3
    print('Sorry Ronald cannot do this operations')

x %= 4 # x = x % 4
print(x)

x /= 3 # x = x / 3
print(x)
print('%.3f'%(x)) # format x at 3-decimal points

y **=2 # y = y ** 2
print(y)
z = pow(y,2)
print(z)

