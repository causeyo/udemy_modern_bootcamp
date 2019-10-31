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

# Lame function that returns a list of beats.  
# Only runs 100 times
def current_beat():
    max = 100
    nums = (1,2,3,4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

# Infinite Generator - returns one beat a time, no list used!
def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1
