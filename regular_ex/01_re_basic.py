# import regex module
import re

# define phone number regex
# 'r' stands for 'raw', it is needed to avoid using escape chars
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with regex pattern 'search' finds only first match
res = pattern.search('Call me at 415 555-4242 or 415 675-4532')
print(res) # returns match object
print(res.group())

# 'findall' to match all occurrences, returns list object
res = pattern.findall('Call me at 415 555-4242 or 415 675-4532')
print(res)

"""
we can use following syntax:
re.search(r'\d{3} \d{3}-\d{4}', 'Call me at 415 555-4242 or 415 675-4532').group()

but with each check it compiles pattern which can be compiled once at the beggining
"""