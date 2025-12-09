"""Write a class CryptoWallet with a private balance.
Perform transactions only if digital signatures (simulated) are valid.
Prevent any direct modification of balance."""

class CryptoWallet:
    def __init__(self, balance):
        self.__balance = balance

    def __verify_signature(self, signature):
        return signature == "valid"

    def deposit(self, amount, signature):
        if self.__verify_signature(signature):
            if amount > 0:
                self.__balance += amount
                print("Deposit successful.")
        else:
            print("Invalid signature.")

    def withdraw(self, amount, signature):
        if self.__verify_signature(signature):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid amount.")
        else:
            print("Invalid signature.")

    def get_balance(self):
        return self.__balance


wallet = CryptoWallet(500)
wallet.deposit(200, "valid")
wallet.withdraw(100, "invalid")
print(wallet.get_balance())
