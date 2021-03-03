class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def total_class_size(self):
        class_ = 0
        for student in self.students.values():
            class_ += student.size
        return class_
