# super():
#     super() in Python is used to call methods from a parent (super) class.
#     It’s most commonly used in inheritance to:
#         reuse parent logic
#         extend behavior instead of rewriting everything

# Basic Idea
# super() gives you access to the parent class methods

#without super you would have to keep writing the same code
# class Shape:
#     def __init__(self,color,is_filled):
#         pass

# class Circle(Shape):
#     def __init__(self,color,filled,radius):
#         self.color = color
#         self.filled = filled
#         self.radius = radius

# class Square(Shape):
#     def __init__(self,color,filled,width):
#         self.color = color
#         self.filled = filled
#         self.width = width

# class Triangle(Shape):
#     def __init__(self,color,filled,width,height):
#         self.color = color
#         self.filled = filled
#         self.width = width
#         self.height = height


# with super
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2") #we can also extend the functionality
    

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")

circle = Circle("Red",True,5)
square = Square("Blue",False,6)
triangle = Triangle("Green",False,5,6)

# circle.describe()
# square.describe()
triangle.describe()
