

class circle:
    
   def __init__(self, radius):
       self.radius = radius
   def area(self):
       self.area = 3.14 * self.radius**2
       print(self.area)
   def perimeter(self):
       self.perimeter = 2 * 3.14 * self.radius
       print(self.perimeter)
       
obj = circle(6)
obj.area()
obj.perimeter()
    
    
           

