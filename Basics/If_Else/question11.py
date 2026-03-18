# Using ONLY a single list comprehension with inline if-else, transform
# the list: data = [15, -3, 0, 42, -8, 7, 100, -50, 33] Rules (applied in this
# order with ternary chaining): - Negative numbers → replace with 0 -
# Numbers divisible by both 3 and 5 → replace with 'FizzBuzz' -
# Numbers divisible by 3 → replace with 'Fizz' - Numbers divisible by 5
# → replace with 'Buzz' - All other positives → keep as-is

data = [15, -3, 0, 42, -8, 7, 100, -50, 33]

result = ["FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else 0 if x < 0 else x for x in data]
print(result)
