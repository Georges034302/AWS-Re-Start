# for-loop syntax:
#
# for <value> in <range>:       
#   <code>
# the for loop will select a value at a time from beginning of the range until the end of the range)

# Req: print all values from 1 to 10 on separate lines
for e in range(1,11):
    print(e)

# Req: print all values from 1 to 10 at the same line
for e in range(1,11):
    print(e,end=' ')
print()