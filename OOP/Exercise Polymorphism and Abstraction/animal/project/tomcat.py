from project.cat import Cat


class Tomcat(Cat):
    class_name = 'Tomcat'
    gender = 'Male'

    def __init__(self,name: str, age: int):
        super().__init__(name,age, Tomcat.gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {Tomcat.gender} {Tomcat.class_name}"

    def make_sound(self):
        return "Hiss"





