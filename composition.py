class Animal:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


class Dog:
    def __init__(self, animal, sound):
        self.animal = animal
        self.sound = sound
        

    def get_sound(self):
        return self.sound

    def get_color(self):
        return self.animal.color

def get_something():

    my_color = "red"
    my_weight = 4
    sound =  "mow"

    my_animal = Dog(Animal(my_color, my_weight), sound)
    print(my_animal.get_sound())
    print(my_animal.get_color())
get_something()


