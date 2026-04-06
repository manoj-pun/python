# Aggregation:
#     Aggregation in Python is a concept from Object-Oriented Programming (OOP) that describes a 
#     "has-a" relationship between objects — but with a key twist:
#         The contained object can exist independently of the container.

# Simple Definition
#     Aggregation = One object uses another object, but does NOT own it.

# Real-Life Analogy
#     Think of:
#         A Department has Teachers
#         But teachers can exist without that department

class Library: #library can exists without book
    def __init__(self,name): 
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.author} by {book.title}"for book in self.books]

class Book: #book can exists without library
    def __init__(self,title,author):
        self.title = title
        self.author = author

library = Library("Kaiser Library")

book1 = Book("Manoj","Book1")
book2 = Book("Pun","Book2")

library.add_book(book1)
library.add_book(book2)

print(library.name)
for book in library.list_books():
    print(book)


