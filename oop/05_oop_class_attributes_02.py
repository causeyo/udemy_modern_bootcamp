class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError("you can not have a {} pet".format(species))
        self.name = name
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
tiger = Pet("Wyatt", "tiger")
Pet.allowed.append("pig")
id(cat.allowed)
id(dog.allowed)
id(Pet.allowed)

# if 'allowed' variable will be used only within __init__ we can make it like this:
"""
class Pet:
    def __init__(self, name, species):
        allowed = ['cat', 'dog', 'fish', 'rat']
        if species not in allowed:
            raise ValueError("you can not have a {} pet".format(species))
        self.name = name
        self.species = species
"""

#if we want protect attribute against overwrite we can do it like this:
"""
class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError("you can not have a {} pet".format(species))
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError("you can not have a {} pet".format(species))
        self.species = species
"""


class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs