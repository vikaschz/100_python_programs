"""
1. Create a class Student with attributes name and age.
Create one object and print both values.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Vikas", 21)
print("Student:", s1.name, "\nAge: ", s1.age)
