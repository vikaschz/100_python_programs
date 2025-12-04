"""
14. Implement a class Vector (2D vector) with: x, y
Overload + operator to add two vectors
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overload + operator
    def __add__(self, other):
        # add corresponding components and return new Vector
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage
v1 = Vector(2, 5)
v2 = Vector(4, -1)

v3 = v1 + v2   # internally calls v1.__add__(v2)
print(v3)      # Vector(6, 4)
