"""
Create a base class Animal with sound().
Derive Dog, Cat, and Cow classes and override sound() in each class.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


class Cow(Animal):
    def sound(self):
        return "Moo!"


animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(f"{animal.name} says: {animal.sound()}")

