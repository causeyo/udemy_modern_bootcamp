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
    counter = 1
    while counter < count:
        yield num
        num += num
        counter += 1

default_multiples = get_multiples()

for i in default_multiples:
    print(i)