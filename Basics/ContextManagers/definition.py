# File handling without context managers:
#     1.Open a file
#     2.File operations
#     3.Close file

# Lets say we want to save some textbooks title to textfile

# so we can do like this:
# file = open("books.txt","w")
# file.write("The Hunger Games\n")
# file.write("The Great Gatsby\n")
# file.write("The Maze Runner\n")
#see here we have not closed the file,since file is not closed the contents should not have been written on the books.txt
# and the contents stays on memory buffer and until its not closed it stays on memory buffer but not on books.txt but our
# CPython(standard python interpreter) does the file.flush() itself meaning pushed to disk immediately, file stays open
# however without closing the file is a bad practise.
# So we use Context Managers that handles the close() automatically even when error happens
# Context Managers:
#   A context manager is any object that implements:
        # __enter__() → runs at the start of the with block
        # __exit__() → runs at the end of the block (even if an error occurs)  

#And also when the error occurs in the above code like below:
# file = open("books.txt","w")
# file.write("The Hunger Games\n")
# file.write("The Great Gatsby\n")
# 1/0 #so this is error and the above two titles should have to stay on the memory buffer not on the books.txt but CPython calls the flush()
# #automatically and two titles are eventually seen on the books.txt and this could also be handled by Context Managers
# file.write("The Maze Runner\n")

#The above code with context managers:
# with open("books.txt","w") as file: #file is kind of like variable
#     file.write("The Hunger Games\n")
#     file.write("The Great Gatsby\n")
#     file.write("The Maze Runner\n")
#     #now you can just run it and it will handle the close itself

with open("books.txt","w") as file:
    file.write("The Hunger Games\n")
    file.write("The Great Gatsby\n")
    1/0
    file.write("The Maze Runner\n")
