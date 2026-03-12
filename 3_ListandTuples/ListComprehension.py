#list comprehension — this is one of the most Pythonic and powerful ways to create lists.

# Basic Syntax
# new_list = [expression for item in iterable if condition]
# expression → value to store in the new list
# item → variable representing each element in the iterable
# iterable → list, tuple, range, etc.
# if condition → optional filter


# squares = []
# for x in range(5):
#     squares.append(x**2)

# print(squares)

#for the same above code using list comprehension
# squares = [x**2 for x in range(5)]
# print(squares)


#with condition
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)


#Using if-else in Expression
# labels = ["even" if x%2==0 else "odd" for x in range(5)]
# print(labels)


#Nested Loops (Flattening)
# pairs = [(x,y) for x in [1,2,3] for y in [4,5]]
# print(pairs)
# #Equivalent to nested for loops:
# pairs = []
# for x in [1,2,3]:
#     for y in [4,5]:
#         pairs.append((x,y))


#with functions
def square(x):
    return x**2

squares = [square(x) for x in range(5)]
print(squares)