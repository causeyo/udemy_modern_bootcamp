"""
class methods
- dunder methods should be at the top
"""

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def initials(self):
        return "{}.{}.".format(self.first[0], self.last[0])

    def eats(self, item):
        return "{} eats {}".format(self.first, item)

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return "Happy {}th birthday {}".format(self.age, self.first)



user1 = User("Phil", "Goodman", 72)
print(user1.full_name())
print(user1.initials())
print(user1.eats("wurst"))
print(user1.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)


class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance