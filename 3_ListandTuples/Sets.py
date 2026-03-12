#A set in Python is an unordered collection of unique elements. 
# Sets are extremely useful when you want no duplicates and fast membership checks.

# fruits = {"apple", "banana", "mango"}
# print(fruits) #Sets are unordered, so elements may appear in any order.

#Set operations
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print(A | B)  # Union 
# print(A & B)  # Intersection 
# print(A - B)  # Difference 
# print(A ^ B)  # Symmetric difference 


#Adding elements
# fruits = {"apple", "banana"}
# fruits.add("mango")
# print(fruits)


#Add multiple elements
# fruits = {"apple", "banana"}
# fruits.update(["grape", "orange"])
# print(fruits)


#removing elements
fruits = {"apple", "banana", "mango"}

# fruits.remove("kiwi")  # Error if element not present
fruits.discard("kiwi")   # No error if element not present
print(fruits)
