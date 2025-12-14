"""
Create an abstract class Shape with an abstract method area().
Implement Triangle and Square.
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


triangle = Triangle(10, 6)
square = Square(4)

print("Triangle Area:", triangle.area())
print("Square Area:", square.area())
