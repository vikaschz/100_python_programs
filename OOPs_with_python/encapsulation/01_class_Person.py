"""Create a class Person with a private variable __age.
Add getter and setter methods that ensure age is never negative."""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative!")

    def get_age(self):
        return f"The age of the person is: {self.__age}"


p1 = Person("Steve", 25)
p1.set_age(96)
print(p1.get_age())
