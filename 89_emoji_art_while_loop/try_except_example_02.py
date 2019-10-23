# first version with different exceptions


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err) # prints original error text
    else:
        print("{} divide by {} is {}".format(a, b, result))


print(divide(7, 0))
print(divide("text", 7))

# more general solution with tuple of errors

def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("some problem occurred")
        print(err)
    else:
        print("{} divide by {} is {}".format(a, b, result))

print(divide(7, 0))
print(divide("text", 7))