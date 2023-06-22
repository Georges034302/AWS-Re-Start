# Read a decimal between 0 and 255 from STDIN
# Convert this decimal to 8-bits binary
# Show the 8-bits binary

n = input("n = ")
while not(n.isnumeric()):
    n = input("n = ")

N = int(n)

mylist = []     # placeholder empty list
zeroes = [0,0,0,0,0,0,0,0]

while N > 0:
    mylist.append(N%2)
    N = int(N/2)
reverse = list(reversed(mylist))
binary = zeroes[len(reverse):len(zeroes)] + reverse
print(binary)