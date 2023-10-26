name = 'Tom'
balance = 125.785

#Req: How can we print the following output ???
#   <name> has $<balance>

# Method 1:
print(name,'has $',balance)

# Method 2:
print(name+' has $'+str(balance))

# Method 3:
print('%s has $%f'%(name,balance))
print('%s has $%.2f'%(name,balance))
print('%10s has $%15.2f'%(name,balance))
print('%-10s has $%-15.2f'%(name,balance))

# Method 4:
print('{} has ${}'.format(name,balance))
print('{} has ${:.2f}'.format(name,balance))
print('{:8} has ${:12.4f}'.format(name,balance))
print('{:<8} has ${:<12.4f}'.format(name,balance))
print('{:>8} has ${:>12.4f}'.format(name,balance))
print('{:^8} has ${:^12.4f}'.format(name,balance))
print('{:*^9} has ${:$^12.4f}'.format(name,balance))

# Method 5: f-string
print(f'{name} has ${balance}')
print(f'{name:11} has ${balance:15.4f}')
print(f'{name:<11} has ${balance:<15.4f}')
print(f'{name:#<11} has ${balance:-<15.4f}')
print(f'{name:@^11} has ${balance:%^15.4f}')
