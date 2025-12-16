"""
Create an abstract class Account with interest().
Implement SavingsAccount and CurrentAccount.
"""

from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def interest(self):
        pass


class SavingsAccount(Account):

    def __init__(self, balance, in_rate):
        self.balance = balance
        self.rate = in_rate

    def interest(self):
        return self.balance * self.rate


class CurrentAccount(Account):

    def __init__(self, balance, in_rate):
        self.balance = balance
        self.rate = in_rate

    def interest(self):
        return self.balance * self.rate


s = SavingsAccount(10000, 0.1)
c = CurrentAccount(10000, 0.04)

print("Savings interest:", s.interest())
print("Current interest:", c.interest())
