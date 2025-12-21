# Menu-Driven Question Template
"""2. Menu-Driven Animal Sound Simulator
Create a class Animal with a method sound(). Subclasses: Dog, Cat, Cow.
Menu options:
1. Choose animal
2. Produce sound
3. Exit
"""


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Dog 🐕 → Bark (woof, woof)"


class Cat(Animal):
    def sound(self):
        return "Cat 🐈 → Meow (meow, purr)"


class Cow(Animal):
    def sound(self):
        return "Cow 🐄 → Moo (moo, moo)"


animal = None
while True:
    print("\n---- Animal Sound Simulator ----")
    print("1. Choose animal")
    print("2. Produce sound")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n1. Dog\n2. Cat\n3. Cow")
        choice_animal = input("choose Animal: ")
        if choice_animal == "1":
            animal = Dog()
            print("Dog selected.")
        elif choice_animal == "2":
            animal = Cat()
            print("Cat selected.")
        elif choice_animal == "3":
            animal = Cow()
            print("Cow selected.")
        else:
            print("Invalid choice")

    elif choice == "2":
        if animal is None:
            print("Please choose an animal first.")

        else:
            print(animal.sound())

    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
