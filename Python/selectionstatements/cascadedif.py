# cascaded-if (sample) syntax:
#
# if <condition 1>:
#   <code 1>
# elif <condition 2>:
#   <code 2>
#
# ...........
# ...........
# elif <condition n-1>
#   <code n-1>
# else:
#   <code n>

# Req: Check the number of arguments used in this script as follows:
#   - if no arguments are given, show the script name
#   - if one argument is given show the argument
#   - if many arguments are given show the list of arguments

import sys 

if len(sys.argv) == 1:
    print(sys.argv[0])
elif len(sys.argv) == 2:
    print(sys.argv[1])
else:
    print(sys.argv)
    
    