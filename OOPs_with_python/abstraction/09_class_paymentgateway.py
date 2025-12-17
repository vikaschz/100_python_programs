"""Create an abstract class PaymentGateway with pay(). Implement UPI, Card, NetBanking."""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentGateway):
    def pay(self, amount):
        print(f"₹{amount} paid using UPI.")


class Card(PaymentGateway):
    def pay(self, amount):
        print(f"₹{amount} paid using Card.")


class NetBanking(PaymentGateway):
    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking.")


p1 = UPI()
p2 = Card()
p3 = NetBanking()

p1.pay(500)
p2.pay(1000)
p3.pay(750)
