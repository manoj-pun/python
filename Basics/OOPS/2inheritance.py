# Inheritance:
# Inheritance is a feature in object-oriented programming that allows a class (child/subclass) to 
# acquire the properties and methods of another class (parent/superclass).

# This helps in:
#     Code reusability – you don’t have to rewrite code.
#     Logical hierarchy – models real-world relationships.
#     Extensibility – you can extend existing behavior.

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("Squeek")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(cat.name)
print(cat.is_alive)

cat.eat()
cat.sleep()
dog.speak()
mouse.speak()