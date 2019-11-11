"""
@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
"""

from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                return "Please only invoke with integers."
        return fn(*args, **kwargs)

    return wrapper


"""
udemy solution

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner
"""