"""
Create a base class Account with balance.
Derive SavingsAccount and CurrentAccount using super() to initialize balance.
"""


class Account:
    def __init__(self, balance):
        self.__balance = balance
        print(f"Account initialized with balance: ₹{self.__balance}")


class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):

        super().__init__(balance)
        self.interest_rate = interest_rate
        print(f"Savings Account created with {self.interest_rate}% interest.")


class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
        print(f"Current Account created with ₹{self.overdraft_limit} overdraft limit.")


savings = SavingsAccount(1000, 3.5)
current = CurrentAccount(500, 1000)
