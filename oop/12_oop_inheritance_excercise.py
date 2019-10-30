class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def speak(self):
        return "Arrrrgh"


troll = NPC("Phil", 7, 12)
print(troll.speak())