# # Class:
# #     A class is like a blueprint for creating objects. It defines attributes (variables) and 
# #     methods (functions) that the objects created from the class can have.

# class Car:
#     wheels = 4 #Class Attributes

#     def start(self): #Methods
#         print("Car is starting")
# # Here:
# #     Car is a class.
# #     wheels is an attribute (shared for all cars here because it's a class attribute).
# #     start() is a method (a function that belongs to the class).

# # Object:
# #     An object is an instance of a class — an actual thing built using the blueprint.

# my_car = Car()  # Create an object of the class Car
# print(my_car.wheels)  # Access attribute
# my_car.start()        # Call method


####################################################################################
# # Instance Attributes:
# #     These are attributes specific to an object, defined inside a special method called __init__.
# #     You don't have to explicitly call __init__ yourself — Python calls it automatically when you create an object.

# class Student:
#     name = "Manoj"

#     def __init__(self):
#         print("This is the demo that everything inside __init__ run without calling it")

# s1 = Student()
# print(s1.name)

# # NOTE: Every method inside the class should have the first parameter `self` that denotes the current object,
# #       because Python automatically passes the object as the first argument when a method is called.
# #       `self` lets the method know WHICH specific object called it, so it can access
# #       that object's data and attributes. Without `self`, the method wouldn't know
# #       which object it belongs to.

####################################################################################
# # Methods:
# #     Methods are functions inside a class that can operate on the object’s data.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width #instance attributes
#         self.height = height #instance attributes
    
#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rect = Rectangle(5, 3)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())


####################################################################################
# Class Attributes vs Instance Attributes
#     Class attributes: shared across all objects.
#     Instance attributes: unique for each object.

# class Dog:
#     species = "Canine"  # Class attribute
    
#     def __init__(self, name):
#         self.name = name  # Instance attribute

# dog1 = Dog("Buddy")
# dog2 = Dog("Max")

# print(dog1.species, dog1.name)
# print(dog2.species, dog2.name)

####################################################################################

####################################################################################