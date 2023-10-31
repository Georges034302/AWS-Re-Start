
def validate_input(value):
    assert str(value).isnumeric(), "Value is not a number"
    
def validate_denominator(value):
    assert value == 0, 'b is zero'