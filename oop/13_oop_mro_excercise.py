class Mother:
    eye_color = "brown"
    hair_color = "dark brown"
    hair_type = "curly"


class Father:
    eye_color = "blue"
    hair_color = "blond"
    hair_type = "straight"


class Child(Mother, Father):
    pass



a = Child()

print(a.eye_color)
