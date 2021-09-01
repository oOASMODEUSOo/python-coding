class Student:
    def __init__(self, student_name, marks):
        self.student = student_name
        self.score = marks

    def Name(self):
        return self.student

    def modify_mark(self):
        new_score = self.score + 10
        return new_score

s1 = Student("Ojas", 80)
print(s1.Name())
print(s1.modify_mark())