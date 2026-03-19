# Python list comprehensions are a concise way to create lists using a single line of code.
# Basic Syntax
    # [expression for item in iterable]
        # expression → what you want to compute for each item
        # item → the variable representing each element
        # iterable → the list, range, or any iterable you are looping over
    # Example:
# squares = [x**2 for x in range(5)]
# print(squares)  


#########################
# With a Condition (If statement)
# [expression for item in iterable if condition]
# Only include items that satisfy the condition.
# Example:
# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares) 


###########################
# With If-Else (Conditional Expression)
# [expression_if_true if condition else expression_if_false for item in iterable]
# Example:
# labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# print(labels)  


##########################
# Multiple For Loops (Nested Loops)
# [expression for item1 in iterable1 for item2 in iterable2]
# Example (all pairs of numbers):
# pairs = [(x, y) for x in [1,2,3] for y in [4,5,6]]
# print(pairs)  


###########################
# Multiple For Loops with Condition
# [expression for item1 in iterable1 for item2 in iterable2 if condition]
# Example:
# pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
# print(pairs)  


##########################
# Combining Multiple Conditions
# [expression for item in iterable if condition1 and condition2]
# Example:
# nums = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
# print(nums) 


#######################
# Flattening a Nested List
# flat_list = [item for sublist in nested_list for item in sublist]
# Example:
# nested_list = [[1,2],[3,4],[5,6]]
# flat_list = [item for sublist in nested_list for item in sublist]
# print(flat_list)  


########################
# Set Comprehension
# {expression for item in iterable if condition}
# Example 1: Squares of numbers 1–10
# squares = {x**2 for x in range(1, 11)}
# print(squares)
# Output (order may vary, because sets are unordered):

# Example 2: Unique vowels in a word
# word = "comprehensions"
# vowels = {char for char in word if char in 'aeiou'}
# print(vowels)  
# Key point: duplicates are automatically removed in sets.


########################
# Dictionary Comprehension
# {key_expr: value_expr for item in iterable if condition}
# Creates a dictionary directly.
# Example 1: Number → square
# squares_dict = {x: x**2 for x in range(1, 6)}
# print(squares_dict)

# Example 2: Word → length (only words longer than 3 letters)
# sentence = "list comprehensions are really powerful tool"
# words = sentence.split()
# word_dict = {word: len(word) for word in words if len(word) > 3}
# print(word_dict)

# Example: Dictionary with conditional values
nums = range(1, 6)
num_type = {x: "even" if x % 2 == 0 else "odd" for x in nums}
print(num_type) 