"""
7. Menu-Driven Employee Salary Calculator
Create class Employee with calculate_salary(). Subclasses: FullTime, PartTime.
Menu options:
1. Enter details
2. Calculate salary
3. Exit
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTime(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTime(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


emp = None

while True:
    print("\n--- Salary Calculator ---")
    print("1. Enter Details")
    print("2. Calculate Salary")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter Employee Name: ")
        print("Type: 1. Full-Time | 2. Part-Time")
        e_type = input("Choice: ")

        if e_type == "1":
            salary = float(input("Enter Monthly Salary: "))
            emp = FullTime(name, salary)
        elif e_type == "2":
            rate = float(input("Enter Hourly Rate: "))
            hours = float(input("Enter Hours Worked: "))
            emp = PartTime(name, rate, hours)
        else:
            print("Invalid type.")

    elif choice == "2":
        if emp:

            total = emp.calculate_salary()
            print(f"\nEmployee: {emp.name}")
            print(f"Total Salary: ₹{total:,.2f}")
        else:
            print("Error: No employee details entered.")

    elif choice == "3":
        print("Exiting...")
        break
