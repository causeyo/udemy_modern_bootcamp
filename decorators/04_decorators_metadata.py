from functools import wraps


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print("you are about to call {}".format(fn.__name__))
        print("Here's the documentation: {}".format(fn.__doc__))
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y


print(add.__doc__)
print(add.__name__)
help(add)