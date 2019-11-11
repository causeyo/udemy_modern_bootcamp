# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return "Hi, I'm {}.".format(name)


@shout
def order(main, side):
    return "Hi, I'd like the {}, with a side of {}, please.".format(main, side)


@shout
def lol():
    return "lol"


print(greet("todd"))
print(order(side="burger", main="fries"))
print(lol())