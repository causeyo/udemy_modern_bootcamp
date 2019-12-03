"""
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
"""


def valid_parentheses(word):
    if word[0] == ")" or word[-1] == "(":
        return False
    return True


"""
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
"""


def reverse_vowels(word):
    vowels = "aeiouy"
    new_word = ""
    word_vowels = [i for i in word if i.lower() in vowels][::-1]
    index = 0
    for i in word:
        if i.lower() in vowels:
            new_word += word_vowels[index]
            index += 1
        else:
            new_word += i
    return new_word


"""
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
"""


def three_odd_numbers(elements):
    index = 0
    while len(elements) > index+2:
        if (elements[index] + elements[index+1] + elements[index+2]) % 2 == 1:
            return True
        index += 1
    return False


"""
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
"""


def mode(elements):
    return sorted(elements, key = elements.count, reverse=True)[0]


"""
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
"""


def running_average():
    result = []
    def count_average(n):
        result.append(n)
        print(sum(result)/len(result))
        return sum(result)/len(result)
    return count_average
