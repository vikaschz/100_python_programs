"""
11. Create a base class Vehicle and a derived class Bike.
Override a method show_info() in Bike.
"""

class Vehicle:

    def show_info(self):
        print("vehicle started")
        print("vehicle stopped")

class Bike(Vehicle):
    def show_info(self):
        print("Bike started")
        print("Bike stopped")

b1 = Bike()
b1.show_info()