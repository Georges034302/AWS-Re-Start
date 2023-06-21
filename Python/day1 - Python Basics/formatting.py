name = "Tom"
balance = 125.295

# Method 1: Concatunate using +
print(name+" has $"+str(balance))

#Method 2: print values next to each other
print(name+" has $",balance)

#Method 3: use formatting modes %s %f %d
print("%s has $%f"%(name,balance))
print("%s has $%.2f"%(name,balance))
print("%10s has $%15.2f"%(name,balance))
print("%-10s has $%-15.2f"%(name,balance))

#Method 4: use the format() function from string
print("{} has ${}".format(name,balance))
print("{} has ${:.2f}".format(name,balance))
print("{:10} has ${:15.2f}".format(name,balance))
print("{:<10} has ${:<15.2f}".format(name,balance))
print("{:>10} has ${:>15.2f}".format(name,balance))
print("{:_>10} has ${:$>15.2f}".format(name,balance))
print("{:^10} has ${:^15.2f}".format(name,balance))
print("{:*^10} has ${:#^15.2f}".format(name,balance))

#Method 5: using the f command (also works with formatting modes)
print(f'{name} has ${balance}')
print(f'{name:>10} has ${balance:<10.4f}')
print(f'{name:#^10} has ${balance:$^15.4f}')