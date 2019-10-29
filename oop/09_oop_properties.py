class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative")

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

# such setter is sketchy, as two attrs
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


phil = Human("Phil", "Goodman", 42)
print(phil.age)
phil.age = 33
print(phil.age)
print(phil.full_name)
phil.full_name = "Fil On"
print(phil.full_name)
print(phil.__dict__)