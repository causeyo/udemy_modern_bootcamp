###### FIRST EXAMPLE ##########
print("\n==============FIRST EXAMPLE==============\n")

nums = [2,4,6,8,10]

doubles = map(lambda x: x**2, nums)

print(doubles) # returns map object
print(list(doubles)) # returns result -> list of numbers
print(list(doubles)) # returns empty list

# usually following syntax is in use
doubles = list(map(lambda x: x**2, nums))
print(doubles)
print(doubles)

###### SECOND EXAMPLE ##########
print("\n==============SECOND EXAMPLE==============\n")

people = ["Phil", "Tom", "Mike"]
print("people list before using map function {}: ".format(people))

peeps = list(map(lambda name: name.upper(), people))
print("people list after using map function {}: ".format(peeps))

print("\n==============THIRD EXAMPLE==============\n")

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last':'Steele'}
]

print("names dict which will be used within map function: {}".format(names))

first_names = list(map(lambda x: x['first'], names))

print("names list created within map function: {}".format(first_names))

