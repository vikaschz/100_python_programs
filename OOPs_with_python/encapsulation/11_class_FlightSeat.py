"""Create a class FlightSeat with private variables __is_booked and __passenger_name.
Booking should only be possible if the seat is free.
Cancellation should reset both variables safely."""


class FlightSeat:
    def __init__(self):
        self.__is_booked = False
        self.__passenger_name = None

    def book_seat(self, passenger_name):

        if self.__is_booked:
            print(f"❌ Error: Seat is already booked by {self.__passenger_name}.")
            return False

        else:
            self.__is_booked = True
            self.__passenger_name = passenger_name
            print(f"✅ Success: Seat booked for {self.__passenger_name}.")
            return True

    def cancel_booking(self):

        if not self.__is_booked:
            # Seat is already free
            print("❌ Error: Seat is already free, nothing to cancel.")
            return False
        else:
            # Seat is booked, proceed with cancellation
            passenger = self.__passenger_name
            self.__is_booked = False
            self.__passenger_name = None
            print(f"✅ Success: Booking for {passenger} has been cancelled.")
            return True

    def get_status(self):

        if self.__is_booked:
            return f"Seat Status: BOOKED by '{self.__passenger_name}'"
        else:
            return "Seat Status: FREE"


# 1. Create a new seat
seat1A = FlightSeat()
print(seat1A.get_status())

# 2. Successfully book the seat
seat1A.book_seat("vikas")
print(seat1A.get_status())

# 3. Attempt to book the seat again (should fail)
seat1A.book_seat("shivam")
print(seat1A.get_status())

# 4. Successfully cancel the booking
seat1A.cancel_booking()
print(seat1A.get_status())
# 5. Attempt to cancel a free seat (should fail)
seat1A.cancel_booking()
seat1A.book_seat("shivam")
