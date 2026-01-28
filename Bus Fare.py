class Vehicle:
    ans = int(input("How many tickets do you want?:"))
    def __init__(self, capacity):
        self.capacity = capacity

    def price(self):
        return self.capacity * 100

class Bus(Vehicle):
    def price(self):
        total_price = super().price()
        maintenance_charge = total_price * 0.10
        final_fare = total_price + maintenance_charge
        return final_fare
    
    
bus = Bus(50)
final_bus_fare = bus.price()
print(final_bus_fare)
      