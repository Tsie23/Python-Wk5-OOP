class Vehicle:
    """Base class for vehicles."""
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving!")

class Helicopter(Vehicle):
    """Helicopter class with altitude attribute."""
    def __init__(self, altitude):
        self.altitude = altitude  # Altitude in meters
    
    def move(self):
        print(f"🚁 Helicopter is hovering at {self.altitude} meters!")

class Boat(Vehicle):
    def move(self):
        print("🚢 Boat is sailing!")