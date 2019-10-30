"""
iterator - an object that can be iterated upon.
An object which returns data, one element at a time when next() is called on it

iterable - an object which will return an iterator when iter() is called on it

When next() is called on an iterator, the iterator returns the next item.
It keeps doing so until it raises a StopIteration error.


"HELLO" is an iterable, but it is not an iterator

iter("HELLO") returns an iterator
"""

# iteration example -> string
name = "Philon"

it = iter(name) # iterator object returned

print(next(it)) # P
print(next(it)) # h
print(next(it)) # i
print(next(it)) # l
print(next(it)) # o
print(next(it)) # n
# print(next(it)) # -> StopIteration error

# iteration example -> list
nums = [1, 2, 3]

nums_it = iter(nums)

print(next(nums_it)) # 1
print(next(nums_it)) # 2
print(next(nums_it)) # 3
# print(next(nums_it)) # -> StopIteration error
