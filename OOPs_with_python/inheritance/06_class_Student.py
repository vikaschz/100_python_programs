"""
Create a base class Student. Derive EngineeringStudent and further derive CSEStudent.
Demonstrate multilevel inheritance.
"""


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")


class EngineeringStudent(Student):
    def __init__(self, name, student_id, college_name):

        super().__init__(name, student_id)
        self.college_name = college_name

    def display_eng_info(self):
        print(f"College: {self.college_name}")


class CSEStudent(EngineeringStudent):
    def __init__(self, name, student_id, college_name, primary_language):

        super().__init__(name, student_id, college_name)
        self.primary_language = primary_language

    def display_full_profile(self):

        self.display_student_info()
        self.display_eng_info()
        print(f"Primary Programming Language: {self.primary_language}")


student= CSEStudent("Ram", "2TG21CS85", "Indian Tech Institute", "Python")

print("--- CSE Student Profile ---")
student.display_full_profile()
