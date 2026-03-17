#lambda
# A lambda function in Python is a small anonymous function (a function without a name) that is written in one line.

#Syntax
# lambda parameters : expression

# Normal Function vs Lambda Function
# def add(a, b):
#     return a + b

# print(add(5, 3))
# def creates the function
# add is the function name
# return sends the result back

#Lambda version
# add = lambda a, b: a + b
# print(add(5, 3))

#Lambda Functions
# 1.Can have multiple parameters
# 2.Must be written on a single line
# 3.Lamda don't use return statement unlike regular function because it automatically returns the result of the operation
# 4.Lambda don't have a name like the regular function


def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def transform_list(nums_list,transform_item):
    print(nums_list)
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0,transformed_1]

mylist = [2,3]
transform_list(mylist,cube)