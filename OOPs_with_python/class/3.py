"""
3. Write a class Rectangle with length and width.
Add a method to calculate area.
"""


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


r1 = Rectangle(5, 3)
print("Rectangle area:", r1.area())

