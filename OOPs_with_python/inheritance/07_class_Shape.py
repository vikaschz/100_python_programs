"""
Create a base class Shape with area(). Derive Circle, Rectangle, and Triangle classes.
"""

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5), 
    Rectangle(10, 5), 
    Triangle(8, 4)
]

for shape in shapes:

    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")