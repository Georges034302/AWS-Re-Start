# while-loop syntax:
#
# <iterator>
# while <iterator compare to sentinel>:
#   <code>
#   <update iterator>

# Req: print all values from 1 to 10 on separate lines

i = 1 
while i <= 10:
    print(i)
    i += 1
    
# Req: print all values from 1 to 10 at the same line
i = 1 
while i <= 10:
    print(i,end= ' ')
    i += 1
print()
    