# lambda in Python is a way to create small, anonymous functions (functions without a name). 
# They are often used inline with other functions that expect a function as an argument.

# Syntax of lambda
# lambda arguments: expression
# arguments → parameters you pass to the function
# expression → single expression whose result is returned automatically
# No return statement is needed
# The function is anonymous (no def name)

# Example:
# def add(x,y):
#     return x + y
# print(add(4,5))

#the above code is written in lambda in following ways
# add = lambda x,y: x+y
# print(add(4,6))


#####lambda commonly works with??
# 1.map()
# Applies a function to every element of an iterable.
# Syntax:
# map(function, iterable)
# function → a function (can be lambda) applied to each element
# iterable → list, tuple, string, etc.
# Returns a map object (convert to list or tuple to see values)
# Example:
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared) 

#or without lambda
# def square(n):
#     return n*n
# n = [1,2,3,4,5]

# y = list(map(square,n))
# print(y)

# 2.filter()
# Filters elements of an iterable based on a condition.
# Syntax:
# filter(function, iterable)
# function → returns True or False for each element
# iterable → list, tuple, etc.
# Returns a filter object (convert to list to see values)
# Example:
# nums = [1, 2, 3, 4, 5]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  

# 3.reduce() (from functools)
# Reduces an iterable to a single value by applying a function cumulatively.
# Syntax:
# from functools import reduce
# reduce(function, iterable, initializer=None)
# function → takes two arguments and returns a single value
# iterable → list, tuple, etc.
# initializer → optional starting value
# Example:
# from functools import reduce
# nums = [1, 2, 3, 4]
# sum_all = reduce(lambda x, y: x + y, nums)
# print(sum_all)  

# Here is how the above code works:
# reduce does this step by step:
# 1.Take the first two elements: 1 and 2
# x = 1, y = 2
# result = x + y = 3
# 2.Take the result from previous step (3) and the next element (3):
# x = 3, y = 3
# result = x + y = 6
# 3.Take the result from previous step (6) and the next element (4):
# x = 6, y = 4
# result = x + y = 10
# No more elements → final result = 10

