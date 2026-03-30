# Multilevel Inheritance:
#     Definition: A child class inherits from a parent, and then another child inherits from that child.
#     Forms a chain of inheritance.

class Animal: #Grandparent
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey(Animal): #Parent
    def flee(self):
        print("This animal is fleeing")

class Preditor(Animal): #Parent
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey): #Now rabbit class can inherit all the methods from the animal and prey
    pass

class Hawk(Preditor): #Now hawk class can inherit all the methods from the animal and preditor
    pass

class Fish(Prey,Preditor): #Now fish class can inherit all the methods from the animal,prey and preditor
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

rabbit.eat()
hawk.sleep()
fish.eat()