first_zip = zip([1, 2, 3], [4, 5, 6])

list(first_zip)
# [(1, 4), (2, 5), (3, 6)]

dict(first_zip)
# {1: 4, 2: 5, 3: 6}

five_by_two = [(1, 2), (2, 4), (3, 6), (4, 8)]

list(zip(*five_by_two))
# [(1, 2, 3, 4), (2, 4, 6, 8)]

#### COMPLEX ZIP ########
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# how to achieve -> final_grades = {'dan': 98, 'ang': 91, 'kate': 78}
#### METHOD 1 ########

final_grade = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# {'ang': 91, 'kate': 78, 'dan': 98}

#### METHOD 2 ########
# more traditional way with using 'map'
final_grades_01 = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

dict(final_grades_01)
# {'dan': 98, 'ang': 91, 'kate': 78}

### DIY EXAMPLE ###
## METHOD 01 ##

def interleave(str1, str2):
    ziplist = list(zip(str1, str2))
    word = ""
    for elem in ziplist:
        for letter in elem:
            word += letter
    return word

a = interleave("hae", "bcr")
print(a)

## METHOD 02 ##
def interleave01(str1, str2):
    return ''.join(''.join(x) for x in (zip(str1, str2)))

b = interleave("hae", "bcr")
print(b)

#### triple and filter ####
'''
leave values divisible by 4 and then triple rest
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


def triple_and_filter(nums):
    return list(map(lambda x: x*3, (filter(lambda n: n % 4 == 0, nums))))


a = triple_and_filter([1,2,3,4])
print(a)


'''
Write a function called extract_full_name. This function should accept a list of dictionaries 
and return a new list of strings with the first and last name keys in each dictionary concatenated.
 
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(names):
    return list(map(lambda n: n['first'] + " " + n['last'], names))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))
