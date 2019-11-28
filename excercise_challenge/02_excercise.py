def titleize(sentence):
    return " ".join(word[0].upper()+word[1:] for word in sentence.split())


"""
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
"""


def find_factors(number):
    return [elem for elem in range(1, number//2+1) if number % elem == 0].append(number)


"""
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
"""

a = find_factors(10)
print(a)