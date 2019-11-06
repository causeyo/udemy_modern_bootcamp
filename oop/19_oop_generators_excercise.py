#################### FIRST EXCERCISE ####################


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

#################### SECOND EXCERCISE ####################


def yes_or_no():
    d = {0: 'yes',
         1: 'no'}
    count = 0
    while True:
        yield d[count % 2]
        count += 1


booler = yes_or_no()
print(next(booler)) # 1
print(next(booler)) # 2
print(next(booler)) # 1
print(next(booler)) # 2
print(next(booler)) # 1
print(next(booler)) # 2
print(next(booler)) # 1
print(next(booler)) # 2

# alternative solution


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"
