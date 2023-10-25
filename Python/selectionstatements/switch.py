# switch (sample) syntax:
#
# match <value>:
#   case <condition 1> : <code 1>
#
# .....
#   case <condition n> : <code n>
#   case _: <default code>

# Req: read a direction and state the possible freeway

d = input('Direction: ')

match d:
    case 'N': print('Going north on M1')
    case 'S': print('Going south on M7')
    case 'W': print('Going west on M4')
    case 'E': print('Going east on M5')
    case _: print('Unknown direction')