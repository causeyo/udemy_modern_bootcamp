"""
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

sum_up_diagonals(list2) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

sum_up_diagonals(list4) # 68
"""


def sum_up_diagonals(elements):
    step = 0
    result = 0
    for element in elements:
        result += element[step] + element[-1-step]
        step += 1
    return result


"""
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
"""


def min_max_key_in_dictionary(num_dict):
    return [min(num_dict.keys()), max(num_dict.keys())]


"""
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
"""


def find_greater_numbers(elements):
    greater = 0
    for elem1 in elements:
        for elem2 in elements[:elements.index(elem1)]:
            if elem1 > elem2: greater += 1
    return greater


"""
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
"""


def two_oldest_ages(elements):
    return sorted(elements)[-2:]


"""
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
"""


def is_odd_string(text):
    char_sum = 0
    for letter in text:
        char_sum += ord(letter) - 96
    return bool(char_sum % 2)
