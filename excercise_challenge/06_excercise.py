"""
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1
"""


def letter_counter(word):
    word = {k: word.lower().count(k) for k in word.lower()}

    def inner(letter):
        return word[letter]
    return inner


"""
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
"""


def once(fn):
    executed = []

    def inner(*args):
        if not executed:
            executed.append(1)
            return fn(*args)
        return None
    return inner


"""
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

def next_prime():
    i = 1
    while True:
        if i > 1:
            yield i


        i += 1

primes = next_prime()
print([next(primes) for i in range(25)])