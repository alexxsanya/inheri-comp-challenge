class Animal:
    def __init__(self,anim_type="",sound=""):
        self.anim_type = anim_type
        self.sound = sound

    def make_sound(self):
        return self.sound

class Cow(Animal):
    def __init__(self,c_type,sex):
        self.c_type = c_type
        self.sex = sex
        Animal.__init__(self,anim_type="herbivores",sound="Moooooow")


class Dog(Animal):
    def __init__(self,name,color):
        self.name = name
        Animal.__init__(self,anim_type="carnivores",sound="Boo boo")