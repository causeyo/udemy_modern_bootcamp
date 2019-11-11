"""
@double_return
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
"""


def double_return(fn):
    def wrapper(*args, **kwargs):
        i = 0
        result = []
        while i < 2:
            result.append(fn(*args, **kwargs))
            i += 1
        return result

    return wrapper

"""
udemy solution

from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper
"""