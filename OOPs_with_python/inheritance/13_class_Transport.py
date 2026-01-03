"""
Create a base class Transport with fare(). Derive Bus, Train, and Flight classes.
"""

class Transport:
    def __init__(self, distance):
        self.distance = distance

    def fare(self):
        return 0


class Bus(Transport):
    def fare(self):

        total = 2 + (self.distance * 0.5)
        print(f"Bus Fare for {self.distance}km: ${total:.2f}")
        return total


class Train(Transport):
    def __init__(self, distance, coach_class="Sleeper"):
        super().__init__(distance)
        self.coach_class = coach_class

    def fare(self):

        rate = 2.0 if self.coach_class == "AC" else 0.8
        total = self.distance * rate
        print(f"Train Fare ({self.coach_class}) for {self.distance}km: ${total:.2f}")
        return total


class Flight(Transport):
    def __init__(self, distance, fuel_surcharge=50):
        super().__init__(distance)
        self.fuel_surcharge = fuel_surcharge

    def fare(self):

        total = 100 + (self.distance * 5) + self.fuel_surcharge
        print(f"Flight Fare for {self.distance}km: ${total:.2f}")
        return total


travel_options = [Bus(50), Train(300, "AC"), Flight(1200)]

print("--- Travel Fare Estimates ---")
for mode in travel_options:
    mode.fare()
