# 01 - we can pass funcs as args to other funcs


def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x*x*x



print(sum(3, square))
print(sum(3, cube))


# 02 - we can nest functions inside one another
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result


print(greet("Toby"))

# 03 - we can return funcs from other funcs
# from random import choice

def make_laugh_func():
    def get_laugh():
        l = choice(("HAHAHA", "lol", "hihihi"))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())

# 04 - inner functions can access outer function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHA", "lol", "hihihi"))
        return "{} {}".format(laugh, person)

    return get_laugh

laugh_at = make_laugh_at_func("Phil")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
