import numpy as np

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return np.mean(self.marks) > 50


good_student = Student("Jan", [70,100,80])
bad_student = Student("Marian", [40,60,30])

print(good_student.is_passed())
print(bad_student.is_passed())