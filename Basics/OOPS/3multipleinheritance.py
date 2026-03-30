# Multiple Inheritance:
#     Definition: A child class inherits from more than one parent class.
#     Python allows a class to have multiple parent classes.
#     Use case: Combine features from different classes.

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Preditor:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

class Fish(Prey,Preditor): #here fish is multiple inheritance as it inherits from two parent class
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
