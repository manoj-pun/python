# names = ["Manoj","David","Alice"]
# ages = [22,21,23]

# i = 0
# for name in names:
#     print(name,ages[i])
#     i += 1

#zip() is a built-in function used to combine two or more iterables (like lists, tuples, or strings) 
# into a single iterable of tuples, where each tuple contains elements 
# from the input iterables at the same position.


# names = ["Manoj","David","Alice"]
# ages = [22,21,23]

# for name, age in zip(names,ages):
#     print(name,age)


#Unequal Lengths
# If the iterables are of unequal length, zip stops at the shortest iterable:
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b']

# for num,char in zip(list1,list2):
#     print(num,char)

# #or
# print(list(zip(list1, list2)))


#Using zip to Unzip
#You can also reverse the process (unzip) using the * operator:
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)

print(nums)    
print(letters) 