# Use a for loop to build a NEW list containing only numbers divisible by 3 from the list below. Print
# the new list.
# numbers = [4, 9, 15, 22, 33, 41, 45, 60, 7, 18]

numbers = [4, 9, 15, 22, 33, 41, 45, 60, 7, 18]

new_numbers = []

for number in numbers:
    if number % 3 == 0:
        new_numbers.append(number)

print(new_numbers)