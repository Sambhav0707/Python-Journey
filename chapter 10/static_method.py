class Car:
    # A class attribute (constant)
    MILES_PER_KM = 0.621371

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # This is an INSTANCE method. It needs 'self'.
    def display_car(self):
        print(f"This is a {self.brand} {self.model}.")

    # This is a STATIC method. It does not get 'self'.
    @staticmethod
    def kph_to_mph(speed_kph):
        """Converts KPH to MPH."""
        # Note: We cannot use 'self' here.
        # We can, however, access other class attributes like Car.MILES_PER_KM
        return speed_kph * Car.MILES_PER_KM

# --- How to use it ---

# 1. Create an instance (object)
my_car = Car("Toyota", "Camry")

# You use the INSTANCE method on the object
my_car.display_car()  
# Output: This is a Toyota Camry.

# 2. Use the STATIC method
# You call it directly on the CLASS itself
speed_in_mph = Car.kph_to_mph(100)
print(f"100 KPH is equal to {speed_in_mph:.2f} MPH.")
# Output: 100 KPH is equal to 67.21 MPH.

# (You *can* also call it on the instance, but it's less common.
# The instance is completely ignored.)
# speed_in_mph = my_car.kph_to_mph(100)