"""Create an abstract class Notification with send(). Implement SMS, Email, PushNotification."""

from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class SMS(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")


class Email(Notification):
    def send(self, message):
        print(f"Email sent: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notification sent: {message}")


n1 = SMS()
n2 = Email()
n3 = PushNotification()

n1.send("Your OTP is 1234")
n2.send("Welcome to our service")
n3.send("You have a new alert")
