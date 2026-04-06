# Composition:
#     Composition is a strong form of a "has-a" relationship where:
#         One object owns another object
#         The child object cannot exist independently

# Simple Definition
#     Composition = One object is made up of another object (and controls its lifecycle).

# Real-Life Analogy
#     Think of:
#         A House has Rooms
#         If the house is destroyed → rooms don’t exist anymore

class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) #class Car owns Engine
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] #class Car owns Wheel

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}"

car1 = Car("Ford","Mustang",500,18)
car2 = Car("Porsche","CT",600,18)

print(car1.display_car())
print(car2.display_car())