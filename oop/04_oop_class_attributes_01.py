# class attributes - attributes shared by all instances of a class


class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return "{} has logged out".format(self.first)

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


print(User.active_users)
user1 = User("Phil", "Goodman", 72)
user2 = User("Gru", "Sia", 18)
print(User.active_users)
user1.logout()
print(User.active_users)