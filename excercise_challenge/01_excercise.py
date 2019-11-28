def reverse_string(text):
    return text[::-1]


'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''


def list_check(elements):
    return all([isinstance(element, list) for element in elements])


'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def remove_every_other(elements):
    return elements[::2]


'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def sum_pairs(elements, number):
    for first_element in elements:
        index = elements.index(first_element)
        for second_element in elements[index+1:]:
            if first_element + second_element == number:
                return [first_element, second_element]
    return []


'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def vowel_count(word):
    result = {}
    vowels = [letter for letter in word.lower() if letter in 'aeiou']
    for v in vowels:
        if v not in result:
            result[v] = 1
        else:
            result[v] += 1
    return result


'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

