"""
6. Create a class BankAccount with:
attributes: holder_name, balance
method: deposit(amount) → increases balance
method: withdraw(amount) → reduces balance
Test with objects.
"""


class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance
        print(f"balance: {balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")
        print(f"current bank balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawed.")
        print(f"current bank balance: {self.balance}")


b1 = BankAccount("vikas", 500)
b1.deposit(1000)
b1.withdraw(500)
