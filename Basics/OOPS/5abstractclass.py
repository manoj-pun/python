# abstract class:
#     An abstract class in Python is a class that cannot be instantiated directly and 
#     is meant to be inherited by other classes.

# Why use abstract classes?
#     To enforce a structure in child classes
#     To ensure certain methods are always implemented

# How Python supports abstract classes:
#     Python provides this via the built-in module:
#     abc (Abstract Base Classes)

from abc import ABC, abstractmethod

class Vehicle():
    @abstractmethod
    def go(self): #now this method must be implemented if the child inherits from Vehicle
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive car")

    def stop(self):
        print("You stop car")

class Bike(Vehicle):
    def go(self):
        print("You ride bike")

    def stop(self):
        print("You stop bike")

car = Car()
car.go()
car.stop()

bike = Bike()
bike.go()
bike.stop()



