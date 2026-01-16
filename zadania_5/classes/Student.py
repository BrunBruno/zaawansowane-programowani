class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def __str__(self) -> str:
        return f'Student: {self.name}'