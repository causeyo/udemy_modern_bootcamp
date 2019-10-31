def week():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    count = 0
    while count < 7:
        yield weekdays[count]
        count += 1

"""
def week():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in weekdays:
        yield day
    
"""

counter = count_up_to()
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 1
print(next(counter)) # 2