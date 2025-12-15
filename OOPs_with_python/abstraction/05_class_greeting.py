"""
Create an abstract class Greeting with say_hello().
Implement EnglishGreeting and SpanishGreeting.
"""

from abc import ABC, abstractmethod


class Greeting(ABC):

    @abstractmethod
    def say_hello(self):
        pass


class EnglishGreeting(Greeting):
    def say_hello(self):
        print("Hello! Nice to meet you.")


class SpanishGreeting(Greeting):
    def say_hello(self):
        print("¡Hola! Encantado de conocerte.")


eng = EnglishGreeting()
spa = SpanishGreeting()

eng.say_hello()
spa.say_hello()
