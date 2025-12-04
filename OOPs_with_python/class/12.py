"""
12. Create a class School that stores multiple Student objects in a list.
Add method to display all student names.
"""

class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        # list to store Student objects
        self.students = []

    def add_student(self, student):
        # student is a Student object
        self.students.append(student)

    def display_student_names(self):
        print("Students in school:")
        for s in self.students:
            print(s.name)

# Example usage
s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

school = School()
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

school.display_student_names()
