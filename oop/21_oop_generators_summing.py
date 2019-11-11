'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1, count=10):
    counter = 0
    number = num
    while counter < count:
        yield number
        number += num
        counter += 1

default_multiples = get_multiples(2,3)

for i in default_multiples:
    print(i)

"""
solution from course

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num
"""