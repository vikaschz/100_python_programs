"""
Create an abstract class GameCharacter with attack(). Implement Warrior, Archer, Wizard.
"""

from abc import ABC, abstractmethod


class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass


class Warrior(GameCharacter):
    def attack(self):
        print("Warrior attacks with a sword!")


class Archer(GameCharacter):
    def attack(self):
        print("Archer attacks with arrows!")


class Wizard(GameCharacter):
    def attack(self):
        print("Wizard attacks with magic spells!")


characters = [Warrior(), Archer(), Wizard()]

for character in characters:
    character.attack()
