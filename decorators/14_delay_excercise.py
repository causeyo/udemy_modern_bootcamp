"""
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
"""


from functools import wraps
from time import sleep


def delay(t):
    def decorator(f):
        @wraps(f)
        def new_func(*args, **kwargs):
            print("Waiting {}s before running {}".format(t, f.__name__))
            sleep(t)
            return f(*args, **kwargs)
        return new_func
    return decorator


@delay(5)
def say_hi():
    return "hi"

print(say_hi())

"""
from udemy

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner
"""