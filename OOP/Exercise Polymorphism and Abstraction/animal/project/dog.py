from project.animal import Animal


class Dog(Animal):
    class_name = 'Dog'

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {Dog.class_name}"

    def make_sound(self):
        return "Woof!"
