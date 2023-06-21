# cascaded-if statement is a multiple condition statement
# Syntax:
# if <condition 1>:
#     <code 1>
# elif <condition 1>:
#     <code 2>
# elif <condition 3>:
#     <code 3>
# .................
# else:
#     <last code>

import sys

length = len(sys.argv) # argv is a list of arguments 

if length == 1:
    print("Script name: "+sys.argv[0])
elif length == 2:
    print("Script has one argument: "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))
    
