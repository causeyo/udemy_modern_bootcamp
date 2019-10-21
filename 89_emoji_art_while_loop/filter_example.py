# filter object contains only the values that return true to the lambda

###### FIRST EXAMPLE ##########
print("\n==============FIRST EXAMPLE==============\n")

l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))

print(evens)

###### SECOND EXAMPLE ##########
print("\n==============SECOND EXAMPLE==============\n")

names = ["andrew", "phil", "ann", "susan", "alfred"]
a_names = list(filter(lambda n: n[0]=='a', names))
print(a_names)


users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]