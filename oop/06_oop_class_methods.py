# class methods are methods (with @classmethod decorator)
# that are not concerned with instances, but the class itself

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return "there are currently {} active users".format(cls.active_users)

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return "{} is {}".format(self.first, self.age)

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


user1 = User("Phil", "Goodman", 72)
user2 = User("Gru", "Sia", 18)

print(User.display_active_users())


uncle = User.from_string("Uncle,Phil,89")
print(uncle.first)
print(uncle.full_name())
print(uncle)