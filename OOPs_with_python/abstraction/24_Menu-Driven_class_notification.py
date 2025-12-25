"""
9. Menu-Driven Notification System
Create a class Notifier with send(). Subclasses: SMS, Email, PushNotification.
Menu options:
1. Choose notification type
2. Send message
3. Exit
"""

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        """Blueprint for sending a notification."""
        pass


class SMS(Notifier):
    def send(self, message):
        print(f"SMS: Sending text message via Cellular Network...")
        print(f"Content: {message}")


class Email(Notifier):
    def send(self, message):
        print(f"Email: Connecting to SMTP server...")
        print(f"Subject: System Update")
        print(f"Body: {message}")


class PushNotification(Notifier):
    def send(self, message):
        print(f"Push: Sending Firebase Cloud Message to Mobile App...")
        print(f"Alert: {message}")


notifier = None

while True:
    print("\n--- Notification Center ---")
    print("1. Choose Notification Type")
    print("2. Send Message")
    print("3. Exit")

    choice = input("Option: ")

    if choice == "1":
        print("\nChannels: 1. SMS | 2. Email | 3. Push")
        n_type = input("Select Channel: ")

        if n_type == "1":
            notifier = SMS()
            print("Channel set to SMS.")
        elif n_type == "2":
            notifier = Email()
            print("Channel set to Email.")
        elif n_type == "3":
            notifier = PushNotification()
            print("Channel set to Push Notification.")
        else:
            print("Invalid channel.")

    elif choice == "2":
        if notifier:
            msg = input("Enter message to send: ")
            # Polymorphic call
            notifier.send(msg)
        else:
            print("Error: Choose a notification type first.")

    elif choice == "3":
        print("Shutting down notification system...")
        break
    else:
        print("Invalid input.")
