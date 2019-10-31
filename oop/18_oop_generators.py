"""
every generator is iterator
not every iterator is a generator


----------------------------------------------
|     FUNCTIONS    |  GENERATOR FUNCTIONS    |
----------------------------------------------
|     uses RETURN  |      uses YIELD         |
----------------------------------------------
|    returns once  | can yield multipletimes |
---------------------------------------------
|   returns value  |    returns generator    |
---------------------------------------------
"""

# first generator

# generator function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter)) # 1
print(next(counter)) # 2

print(list(counter)) # [3, 4, 5]