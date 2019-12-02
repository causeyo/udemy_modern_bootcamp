def two_list_dictionary(first_list, second_list):
    dict_key = dict.fromkeys(first_list)
    dict_value = dict(zip(first_list, second_list))
    dict_key.update(dict_value)
    return dict_key


"""
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
"""


def range_in_list(elements, x=0, y=None):
    if not y or len(elements) < y:
        return sum(elements[x: ])
    return sum(elements[x: y+1])


"""
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
"""


def same_frequency(x, y):
    return sorted([elem for elem in str(x)]) == sorted([elem for elem in str(y)])


"""
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
"""


def nth(elements, index):
    return elements[index]


"""
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
"""


def find_the_duplicate(elements):
    freq_dict = {i: elements.count(i) for i in elements}
    for key, value in freq_dict.items():
        if value == 2:
            return key
    return None


"""
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
"""
