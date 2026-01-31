class Ferrari():
    def fuel_type(self):
        print("The Fuel Type of a Ferrari is Premium Unleaded Petrol. ")
        
    def max_speed(self):
        print("The Max Speed of a Ferrari is 211 m/h. ")
        
class BMW():
    def fuel_type(self):
        print("The Fuel type of a BMW is Premuim Unleaded Gasoline. ")
        
    def max_speed(self):
        print("The Max Speed of a BMW is 191 m/h. ")
        
obj_F = Ferrari()
obj_B = BMW()


for car_brand in (obj_F, obj_B):
    car_brand.fuel_type()
    car_brand.max_speed()