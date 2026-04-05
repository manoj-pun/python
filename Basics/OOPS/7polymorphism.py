# Polymorphism:
#     Polymorphism in Python means “many forms” — the same interface (function/method/operator) 
#     behaves differently depending on the object.

#     Two ways to achieve Polymorphism:
#         1.Inheritance
#         2.Duck Typing

class Shape:
    pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass

shapes = [Circle(),Square(),Triangle()]

for shape in shapes:
    print(shape)