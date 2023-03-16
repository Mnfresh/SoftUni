from project.animal import Animal


class Cat(Animal):
    class_name = 'Cat'
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {Cat.class_name}"

    def make_sound(self):
        return "Meow meow!"
