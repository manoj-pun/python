# Write code using only list comprehensions (no explicit for loops) to create: (a) all even numbers
# from 1 to 50, (b) squares of all odd numbers from 1 to 20, (c) all pairs (x,y) where x is from
# [1,2,3] and y is from [4,5,6], (d) a flattened version of [[1,2],[3,4],[5,6]].

# (a)
evenNumbers = [x for x in range(1,51) if x % 2 == 0]

# (b)
squareOdd = [x**2 for x in range(1,21) if x % 2 != 0]

# (c)
pairs = [(x, y) for x in [1,2,3] for y in [4,5,6]]

# (d)
flat = [num for sublist in [[1,2],[3,4],[5,6]] for num in sublist]

print(evenNumbers)
print(squareOdd)
print(pairs)
print(flat)



