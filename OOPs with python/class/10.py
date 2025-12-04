# 10. Write a class Calculator with methods for add, subtract, multiply, divide.


class Calculator:

    def add(self, n1, n2):
        return f"{n1} + {n2} = {n1 + n2}"

    def subtract(self, n1, n2):
        return f"{n1} - {n2} = {n1 - n2}"

    def multiply(self, n1, n2):
        return f"{n1} * {n2} = {n1 * n2}"

    def divide(self, n1, n2):
        return f"{n1} / {n2} = {n1 / n2}"


ca1 = Calculator()
print(ca1.add(5, 6))
print(ca1.subtract(20, 15))
print(ca1.multiply(10, 5))
print(ca1.divide(100, 20))
