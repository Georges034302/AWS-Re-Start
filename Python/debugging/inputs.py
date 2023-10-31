import test_inputs as test

a = input('a = ')
b = input('b = ')

def div(a,b):
    test.validate_input(a)
    test.validate_input(b)
    test.validate_denominator(b)
    return int(a)/int(b)

print(div(a,b))