# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#
class Vehicle:
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle 
    def drive(self,speed):
        self.mode="driving"
        self.speed=speed 
        print(f"The {self.bodystyle} is now {self.mode} at {self.speed} mph")   

class Car(Vehicle):
    def __init__(self, enginetype):  
       super().__init__("car")
       self.engine = enginetype
       self.wheels = 4
       self.doors = 4
    def drive(self,speed): 
         super().drive(speed)
         print(f"The {self.engine} car is going at {self.speed}  mph to fast, be careful!")   

class Motorcycle(Vehicle):
    def __init__(self, enginetype,hasssidecar):  
       super().__init__("motorcycle")
       self.engine = enginetype
       if hasssidecar: 
           self.wheels = 3 
       else: 
           self.wheels = 2      
       self.doors = 0
    def drive(self,speed): 
         super().drive(speed)
         print(f"The {self.engine} motorcycle is going at {self.speed}  mph to fast, be careful!")      

Car("mazda")
print(Car("mazda").bodystyle)
print(Car("mazda").engine)
print(Car("mazda").wheels)  
print(Car("mazda").doors)

car1 = Car("gas")
car2 = Car("electricity")
mt1=Motorcycle("gas",True)
print(car1.wheels)
print(car1.doors)
print(mt1.wheels)
print(mt1.bodystyle)
print(mt1.engine)    
car1.drive(80)
car2.drive(60)
mt1.drive(100)
