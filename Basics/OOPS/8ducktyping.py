# Duck Typing:
#     Duck typing is one of the most important (and very “Pythonic”) ways to achieve polymorphism.
                                              
#     What is Duck Typing?
#     “If it looks like a duck and quacks like a duck, it’s a duck.”

#     Python checks:  
#     ❌ NOT: “Is this a Dog or Cat?”
#     ✅ BUT: “Does it have .speak()?”

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False
    def speak(self): #Since car is not animal but it can speak
        print("Honk")

animals = [Dog(),Cat(),Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)