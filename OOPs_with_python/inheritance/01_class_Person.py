"""
Create a base class Person with name and age.
Derive Student and Teacher classes.
Demonstrate hierarchical inheritance.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def details(self):
        super().details()
        print(f"Subject: {self.subject}")


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def details(self):
        super().details()
        print(f"Course: {self.course}")


teacher = Teacher("Claire", 36, "Mathematics")
student = Student("Vikas", 20, "History")

teacher.details()
print()
student.details()
