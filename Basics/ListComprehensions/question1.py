# Create a list of all numbers from 1 to 50 that are divisible by 3 OR by 5,
# but NOT by both (exclusive or).

numbers = [x for x in range(1, 50) if (x % 3 == 0) ^ (x % 5 == 0)]
print(numbers)