"""
Create an abstract class Bank with deposit() and withdraw(). Implement SBI and HDFC.
"""

from abc import ABC, abstractmethod


class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SBI(Bank):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"SBI: Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"SBI: Withdrawn ₹{amount}. Balance: ₹{self.balance}")
        else:
            print("SBI: Insufficient balance!")


class HDFC(Bank):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"HDFC: Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"HDFC: Withdrawn ₹{amount}. Balance: ₹{self.balance}")
        else:
            print("HDFC: Insufficient balance!")


sbi = SBI(5000)
hdfc = HDFC(8000)

sbi.deposit(2000)
sbi.withdraw(3000)

hdfc.deposit(1000)
hdfc.withdraw(9000)
