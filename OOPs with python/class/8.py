# 8. Create a class Circle with radius. Add methods: area(), perimeter()


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius**2

    def perimeter(self):
        return 2 * 3.142 * self.radius


c1 = Circle(5)
print(c1.area())
print(c1.perimeter())
