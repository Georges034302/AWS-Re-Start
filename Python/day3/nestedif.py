# nested-if statement is including one ore more statements
# into the if section or the else section.
# NOTE: there is no limit on how deep nesting can go
# Example Syntax:
# if <condition 1>:
#   <code 1>
#    if <condition 2>:
#        <code 2>
#    else:
#        <code 3>
# else:
#     <last code>

x = input("x = ")

if x.isnumeric():
    if int(x) > 0:
        print(x+" is positive")
    elif int(x) < 0:
        print(x+" is negative")
    else:
        print(x+" is zero")
else:
    print(x+" is not a number")