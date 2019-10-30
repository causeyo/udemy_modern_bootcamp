def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            print(thing)


print("simple example - start \n")

my_for("lol")
my_for([1, 2, 3, 4, 5])

print("simple example - finish \n")

def my_for_with_func(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


def square(x):
    print(x * x)

print("complex example - start \n")

my_for_with_func("lol", print)
my_for_with_func([1, 2, 3, 4, 5], square)

print("complex example - end \n")