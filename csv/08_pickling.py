import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return "{} is a {}".format(self.name, self.species)

    def make_sound(self, sound):
        print("this animal says {}".format(sound))


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat") # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print("{} plays with {}".format(self.name, self.toy))


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
    pickle.dump(blue, file)

# To unpickle something:
# with open("pets.pickle", "rb") as file:
#     zombie_blue = pickle.load(file)
#     print(zombie_blue)
#     print(zombie_blue.play())
