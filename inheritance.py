class Animal:
    def __init__(self,anim_type="",sound=""):
        self.anim_type = anim_type
        self.sound = sound

    def make_sound(self):
        return self.sound