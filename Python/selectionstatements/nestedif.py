# nested-if (sample) syntax:
#
# if <condition 1>:
#   <code 1>
#   if <condition 2>:
#       <code 2>
#   else:
#      <code 3>
# else:
#   <code 4>   

# Req: read x from STDIN as integers
#   - check if x is negative or not
#   - check if x is even or odd (if x is positive)

x = int(input('x = '))

if x < 0:
    print(f'{x} is negative')
else:
    if x%2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')

print('program finished')