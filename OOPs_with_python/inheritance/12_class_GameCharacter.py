"""
Create a base class GameCharacter with attack().
Derive Warrior, Archer, and Mage classes and override attack().
"""
class Shape2:
    def draw(self):
        raise NotImplementedError("Subclass must implement draw()")

class Circle2(Shape2):
    def draw(self):
        print("Drawing Circle")

class Square2(Shape2):
    def draw(self):
        print("Drawing Square")

class Triangle2(Shape2):
    def draw(self):
        print("Drawing Triangle")

def get_shape(choice: str) -> Shape2:
    choice = choice.lower()
    if choice == "circle":
        return Circle2()
    elif choice == "square":
        return Square2()
    elif choice == "triangle":
        return Triangle2()
    else:
        raise ValueError("Unknown shape")

# runtime selection
user_choices = ["circle", "square", "triangle"]

for ch in user_choices:
    shape_obj = get_shape(ch)   # object decided at runtime
    shape_obj.draw()

class GameCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):

        print(f"{self.name} prepares for combat!")


class Warrior(GameCharacter):
    def __init__(self, name, level, weapon_type):
        super().__init__(name, level)
        self.weapon_type = weapon_type

    def attack(self):

        print(f"{self.name} the Warrior swings their {self.weapon_type}! ⚔️")
        print(f"Deals physical damage based on Level {self.level}.")


class Archer(GameCharacter):
    def __init__(self, name, level, arrow_count):
        super().__init__(name, level)
        self.arrow_count = arrow_count

    def attack(self):
        if self.arrow_count > 0:
            self.arrow_count -= 1
            print(f"{self.name} the Archer fires a precise shot! 🏹")
            print(f"Arrows remaining: {self.arrow_count}")
        else:
            print(f"{self.name} is out of arrows!")


class Mage(GameCharacter):
    def __init__(self, name, level, mana):
        super().__init__(name, level)
        self.mana = mana

    def attack(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} the Mage casts Fireball! 🔥")
            print(f"Mana remaining: {self.mana}")
        else:
            print(f"{self.name} doesn't have enough mana!")


party = [
    Warrior("Thorin", 10, "Greatsword"),
    Archer("Legolas", 12, 5),
    Mage("Gandalf", 25, 100),
]

print("--- Encounter Started! ---")
for character in party:
    character.attack()
