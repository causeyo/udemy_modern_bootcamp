# udemy solutions


def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s


def list_check(vals):
    return all(type(l) == list for l in vals)


def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]


def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []


def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}