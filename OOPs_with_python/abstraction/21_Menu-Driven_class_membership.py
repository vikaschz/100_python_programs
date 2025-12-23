"""
6. Menu-Driven Membership System
Create abstract class Member with benefit(). Subclasses: Silver, Gold, Platinum.
Menu options:
1. Choose membership
2. View benefits
3. Exit
"""

from abc import ABC, abstractmethod


class Member(ABC):
    @abstractmethod
    def benefit(self):
        """Each membership tier must define its own benefits."""
        pass


class SilverMember(Member):
    def benefit(self):
        print("Silver Benefits: 5% discount on all purchases and monthly newsletters.")


class GoldMember(Member):
    def benefit(self):
        print("Gold Benefits: 15% discount, free shipping, and priority support.")


class PlatinumMember(Member):
    def benefit(self):
        print(
            "Platinum Benefits: 25% discount, 24/7 dedicated concierge, and VIP lounge access."
        )


current_member = None

while True:
    print("\n--- Membership Management System ---")
    print("1. Choose Membership Tier")
    print("2. View Benefits")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nSelect Tier: 1. Silver | 2. Gold | 3. Platinum")
        tier_choice = input("Choice: ")

        if tier_choice == "1":
            current_member = SilverMember()
            print("Tier set to Silver.")
        elif tier_choice == "2":
            current_member = GoldMember()
            print("Tier set to Gold.")
        elif tier_choice == "3":
            current_member = PlatinumMember()
            print("Tier set to Platinum.")
        else:
            print("Invalid selection.")

    elif choice == "2":
        if current_member:
            current_member.benefit()
        else:
            print("Error: No membership selected. Please choose a tier first.")

    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input, please try again.")
