# Create a list of 10 integers. Write code (without using max, min, or sum) to manually find the
# largest number, the smallest number, and the total. Then compare your answers with the built-in
# functions to confirm they match.

numbers = [1,9,4,7,3,12,-3,89,45,27,32]

# initialize values
largest = numbers[0]
smallest = numbers[0]
total = 0

for number in numbers:
    # find largest
    if number > largest:
        largest = number

    # find smallest
    if number < smallest:
        smallest = number

    # calculate total
    total = total + number

print("Manual Results")
print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)


# Built-in comparison
print("\nUsing Built-in Functions")
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Total:", sum(numbers))


#Pythonic version
numbers = [1, 9, 4, 7, 3, 12, 89, 45, 27, 32]

# Initialize with the first element
largest = smallest = numbers[0]
total = 0

for n in numbers:
    largest = n if n > largest else largest
    smallest = n if n < smallest else smallest
    total += n

print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
