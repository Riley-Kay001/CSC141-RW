# VEHICLES
class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._miles_per_gallon = miles_per_gallon

    @property
    def name(self):
        return self._name
    
# Properties for Range 
    @property
    def range(self):
        return self._fuel_capacity * self._miles_per_gallon
    
    @property
    def cost_per_mile(self):
        return self._cost_per_gallon / self._miles_per_gallon
    
# 4 Different Modes of Transportation 
car = Vehicle("Car", 230, 3.71, 24)
bus = Vehicle ("Bus", 100, 5.00, 13)
airplane = Vehicle ("Airplane", 27000, 8.00, 0.60)
train = Vehicle ("Train", 2000, 2.00, 500)


# 5 Table
print(f"{'Name':<10} {'Range':<10} {'Cost/Mile':<10}")

print(f"{car.name: <10} {car.range: <10} {car.cost_per_mile:<10}")
print("-" * 30)

print(f"{bus.name: <10} {bus.range: <10} {bus.cost_per_mile:<10}")
print("-" * 30)

print(f"{airplane.name: <10} {airplane.range: <10} {airplane.cost_per_mile:<10}")
print("-" * 30)

print(f"{train.name: <10} {train.range: <10} {train.cost_per_mile:<10}")
print("-" * 30)

