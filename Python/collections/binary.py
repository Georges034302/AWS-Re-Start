#Req: Read a decimal number between 0 and 255 from STDIN
#   Convert this decimal to 8-bits binary
#   Show the 8-bits binary

n = int(input('Decimal: '))
bits = []

while n > 0:
    bits.append(n%2)
    n = int(n/2)    
# print(bits)

reverse = list(reversed(bits))
# print(reverse)

zeroes = [0,0,0,0,0,0,0,0,]

binary = zeroes[len(reverse):len(zeroes)] + reverse
# print(binary)

for e in binary:
    print(e,end=' ')
print()