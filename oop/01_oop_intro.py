"""
simple class example
"""


class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Phil", "Goodman", 72)
user2 = User("Gru", "Sia", 18)

print(user1.first)
print(user2.age)


# another simple class
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes