"""
ASSERTS:
- assert is not a function, it is a statement
- assert accepts an expression
- returns None if the expression is truthy
- raises an AssertionError if the expression is falsy
- accepts an optional error message as a second argument
"""


def add_positive_number(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y


add_positive_number(2, 2) # 4
add_positive_number(1, -1) # "Both numbers must be positive!"


def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy"
    ], "this is not a junk food"
    return "NOM NOM NOM I am eating {}".format(food)


eat_junk("pizza")
eat_junk("burger")

# if a python file is run with the -O flag, assertions will not be evaluated
# python -O 01_asserts.py

