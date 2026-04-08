# Magic Methods:
#     These methods let you customize the behavior of your objects with built-in Python operations.
#     Also know as dunder methods(short for double underscore)
#     They are automatically called by the Python's built-in operations like the __init__

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other): #note: other is involved when the operation involves two objects.use other for arithmetic,comparision and bitwise because we need two operands to perform operation
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"

book1 = Book("Python 101", "Alice", 250)
book2 = Book("Deep Learning", "Bob", 320)
book3 = Book("Deep Learning", "Bob", 320)
book4 = Book("Algorithms Unlocked", "David", 480)
book5 = Book("Machine Learning Basics", "Eve", 360)

# print(book1)#now when we do this, it gives the memory address,but we can customize this behaviour using __str__
# print(book1)
###what happens behind the scenes:
    # 1)print() receives an object
    #     When you do:
    #         print(book1)
    #     The print() function doesn’t know how to convert a Book object to a string by default. It internally calls Python’s str() function:
    #         str(book1)
    # 2)str() looks for __str__
    #     Python tries to find a __str__ method on the object:
    #         book1.__str__()
    #     If you defined __str__ (like you did), it executes your method and gets the returned string.
    #     If __str__ is not defined, Python falls back to __repr__.
    # 3)Your __str__ returns a string
    #     In your case:
    #         def __str__(self):
    #             return f"{self.title} by {self.author}"
    #         So Python executes it and gets something like:
    #             "Python 101 by Alice"
    # 4)print() outputs the string
    #     Finally, print() prints the string returned by __str__ to the console.


# print(book2 == book3) #Even though they have the same title,author and numpages it still prints false
# print(book2 == book3) #looks for __eq__


# print(book3 < book4)
# NOTE: if we do not define __lt__ then it looks for its reflected method __gt__ 
#         but if both of them are not defined python raises error:
#         TypeError: '<' not supported between instances of 'Book' and 'Book'
            # Also note that many of the dunder methods has their reflected methods please check that too.

# print(book3 > book4)

# print(book3+book4)

# print("Basics" in book5) #throws error when contains is not defined
# print("Basics" in book5)

print(book4["title"])
print(book4["author"])
print(book4["audio"])




