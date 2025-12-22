"""
3. Menu-Driven Shape Area Calculator
Create a class Shape with area(). Subclasses: Circle, Rectangle, Triangle.
Menu options:
1. Choose shape
2. Calculate area
3. Exit
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shape = None

while True:
    print("\n---- Shape Area Calculator ----")
    print("1. Choose shape")
    print("2. Calculate area")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n1. Circle\n2. Rectangle\n3. Triangle")
        choice_shape = input("Choose a shape: ")

        if choice_shape == "1":
            r = float(input("Enter radius: "))
            shape = Circle(r)
            print("Circle selected.")

        elif choice_shape == "2":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            shape = Rectangle(l, w)
            print("Rectangle selected.")

        elif choice_shape == "3":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            shape = Triangle(b, h)
            print("Triangle selected.")

        else:
            print("Invalid choice.")

    elif choice == "2":
        if shape is None:
            print("Please choose a shape first.")
        else:
            print("Area =", shape.area())

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
