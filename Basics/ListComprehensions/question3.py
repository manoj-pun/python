# Use a single nested list comprehension to flatten this 3-level nested
# list into one flat list of numbers. nested =
# [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]

nested = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]

single_nested = [item for sublist in nested for items in sublist for item in items]
print(single_nested)