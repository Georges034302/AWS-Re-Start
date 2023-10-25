# if-else syntax:
#
# if <condition>:
#   <code 1>
# else:
#   <code 2>

# Req: capture x and y integers from arguments
# check if x < y or not

import sys 

x = int(sys.argv[1])
y = int(sys.argv[2])

if x < y :
    print(f'{x} < {y}')
else:
    print(f'{x} >= {y}')
    
print('program finished')