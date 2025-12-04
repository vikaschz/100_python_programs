"""
7. Create a class Employee with name and salary. Add a method that prints:
Employee <name> earns <salary>
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee {self.name} earns {self.salary}")

#object 1       
e1 = Employee("vikas", 75000)
e1.display()

#object 2       
e2 = Employee("shivam", 75000)
e2.display()