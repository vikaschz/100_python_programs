"""
Create an abstract class Employee with calculate_salary().
Implement FullTimeEmployee and PartTimeEmployee.
"""
from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


# Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Testing the classes
fte = FullTimeEmployee(30000)
pte = PartTimeEmployee(80, 200)

print("Full Time Salary:", fte.calculate_salary())
print("Part Time Salary:", pte.calculate_salary())
