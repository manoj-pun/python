# Using enumerate(), write a comprehension that returns a list of (index,
# value) tuples ONLY for elements at ODD indices in the list. data =
# ['a','b','c','d','e','f','g','h']

data = ['a','b','c','d','e','f','g','h']


odd_elements = [(index, value) for index, value in enumerate(data) if index % 2 != 0]

print(odd_elements)