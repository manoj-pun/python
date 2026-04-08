# What is a class method?
#     A class method is a method that:
#         Works with the class itself (not instance)
#         Takes cls as the first parameter
#         Defined using @classmethod

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa 
        Student.count += 1
        Student.total_gpa += gpa

    def get_details(self):
        return f"{self.name} - {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total student is {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"
    

student1 = Student("Manoj",3)
student2 = Student("David",2)

print(student1.get_details())

print(Student.get_count())

print(Student.get_average_gpa())

