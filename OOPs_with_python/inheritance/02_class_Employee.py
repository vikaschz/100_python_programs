"""
Create a base class Employee with calculate_salary(). 
Derive FullTimeEmployee and PartTimeEmployee and override calculate_salary().
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

employees = [
    FullTimeEmployee("Alice", 55000),
    PartTimeEmployee("Bob", 100, 80)
]

for emp in employees:
    print(f"{emp.name}'s Salary: ₹{emp.calculate_salary()}")