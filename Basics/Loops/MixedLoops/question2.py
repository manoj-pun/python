# Use a while loop INSIDE a for loop: For each number in [2, 3, 5], print its full multiplication table
# from 1 to 10 using the while loop.

numbers = [2,3,5]

for number in numbers:
    j = 1
    print(f"Multiplication of {number}")
    while j <= 10:
        print(f"{number} x {j}: {number * j}")
        j += 1
