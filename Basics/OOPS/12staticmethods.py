# Static methods:
#     Static methods in Python are methods that belong to a class 
#     but don’t depend on the instance (self) or the class (cls).

# Use a static method when:
#     The logic is related to the class
#     But it does NOT need instance data or class data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position): #You define a static method using the @staticmethod decorator
        valid_positions = ["Manager","Developer","Cook"]
        return position in valid_positions
    
print(Employee.is_valid_position("Cook")) #and to call static methods,you don't have to create objects, you could call directly with class

employee1 = Employee("Manoj","Developer")
employee2 = Employee("David","Janitor")

print(employee1.get_details())
print(employee2.get_details())


#######Note there are three methods in python we generally use:
#instance methods
#static methods
#class methods
    
