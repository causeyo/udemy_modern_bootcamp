def square(num):
    return num * num
print(square(9))

def square1(num): return num * num
print(square1(11))

square2 = lambda num: num * num
print(square2(8))

# lambda - has no name - it is like 'anonymous function'

cube = lambda num: num ** 3
cube(3)