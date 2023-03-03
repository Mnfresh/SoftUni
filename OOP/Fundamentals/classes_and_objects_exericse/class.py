class Class:
    __students_count = 22

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < 22:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        total = 0
        for grade in self.grades:
            total += grade

        average = total / len(self.grades)

        return round(average, 2)

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}. Average grade: " \
               f"{self.get_average_grade()}"
