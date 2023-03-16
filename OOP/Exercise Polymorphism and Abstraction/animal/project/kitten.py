from project.cat import Cat


class Kitten(Cat):
    class_name = 'Kitten'
    gender = 'Female'

    def __init__(self,name: str, age: int):
        super().__init__(name,age, Kitten.gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {Kitten.gender} {Kitten.class_name}"

    def make_sound(self):
        return "Meow"
