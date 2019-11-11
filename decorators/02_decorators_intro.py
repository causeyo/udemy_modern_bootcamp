"""
what is DECORATOR?
- decorators are functions
- decorators wrap other functions and enhance/change their behavior
- decorators are examples of higher order functions
- decorators have their own syntax, using '@' - syntactic sugar
"""


def be_polite(fn):
    def wrapper():
        print("nice to meet you!")
        fn()
        print("please be nice to me")
    return wrapper


# def greet():
#     print("my name is phil")
#
#
# greet()
# nice_greet = be_polite(greet)

# syntactic sugar


@be_polite
def greet():
    print("my name is phil")


greet()
