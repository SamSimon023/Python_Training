
# Parent class 1
class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        return f"Charging battery to {self.battery_capacity} kWh."


# Parent class 2
class FuelVehicle:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        return f"Refueling with {self.fuel_capacity} liters of fuel."


# Child class using multiple inheritance
class HybridCar(ElectricVehicle, FuelVehicle):
    def __init__(self, battery_capacity, fuel_capacity):
        ElectricVehicle.__init__(self, battery_capacity)  # Initialize ElectricVehicle
        FuelVehicle.__init__(self, fuel_capacity)        # Initialize FuelVehicle

    def start(self):
        return "HybridCar started using both electric and fuel power."


# Example usage
car = HybridCar(50, 40)  # 50 kWh battery, 40 liters fuel
print(car.start())                # Method from HybridCar
print(car.charge_battery())       # Inherited from ElectricVehicle
print(car.refuel())               # Inherited from FuelVehicle
