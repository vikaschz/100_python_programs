"""
10. Menu-Driven Transport Ticket System
Create a class Transport with book_ticket(). Subclasses: Train, Bus, Flight.
Menu options:
1. Choose transport
2. Book ticket
3. Exit
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def book_ticket(self):
        """Abstract method to handle ticket booking logic."""
        pass
   

class Train(Transport):
    def book_ticket(self):
        print("\n--- Train Ticket Booking ---")
        print("Searching for available Berths...")
        print("Success: Reservation confirmed in Sleeper Class.")


class Bus(Transport):
    def book_ticket(self):
        print("\n--- Bus Ticket Booking ---")
        print("Selecting Window Seat...")
        print("Success: Seat 12A reserved. Ticket sent to mobile.")


class Flight(Transport):
    def book_ticket(self):
        print("\n--- Flight Ticket Booking ---")
        print("Checking Passport details and Baggage allowance...")
        print("Success: Boarding pass generated for Economy Class.")


selection = None


while True:
    print("\n--- Transport Ticket System ---")
    print("1. Choose Transport")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nOptions: 1. Train | 2. Bus | 3. Flight")
        t_type = input("Choose transport: ")

        if t_type == "1":
            selection = Train()
            print("Transport set to Train.")
        elif t_type == "2":
            selection = Bus()
            print("Transport set to Bus.")
        elif t_type == "3":
            selection = Flight()
            print("Transport set to Flight.")
        else:
            print("Invalid selection.")

    elif choice == "2":
        if selection:

            selection.book_ticket()
        else:
            print("Error: Please choose a transport mode first (Option 1).")

    elif choice == "3":
        print("Thank you for using our system. Goodbye!")
        break
    else:
        print("Invalid input, please try again.")

