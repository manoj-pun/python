# enumerate():
# It’s one of the most useful functions when you need both the index and 
# the value while iterating over a list (or any iterable).

# syntax:
# enumerate(iterable, start=0)
# iterable → any iterable (list, tuple, string, etc.)
# start → optional, default is 0. Sets the starting index.

# Basic Example
# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

##############
# Changing the Starting Index
# fruits = ['apple', 'banana', 'cherry']
# for idx, fruit in enumerate(fruits, start=1):
#     print(idx, fruit)

#############
# Convert enumerate to List
# fruits = ['apple', 'banana', 'cherry']
# fruits_enum = list(enumerate(fruits))
# print(fruits_enum)
#Each element becomes a tuple: (index, value).

#############
# With Strings
word = "hello"
for idx, char in enumerate(word):
    print(idx, char)