# Use a for loop to generate a list of 10 random integers (random.randint(1,50)), then use a while
# loop to REMOVE ALL DUPLICATES one at a time until all elements are unique. Print before and
# after.

import random

# Generate 10 random integers
random_integers = []
for i in range(10):
    num = random.randint(1, 20)
    random_integers.append(num)

print("Before removing duplicates:", random_integers)

# Remove duplicates using while loop
i = 0
while i < len(random_integers):
    current = random_integers[i]
    j = i + 1
    while j < len(random_integers):
        if random_integers[j] == current:
            random_integers.pop(j)  # remove duplicate
        else:
            j += 1
    i += 1

print("After removing duplicates:", random_integers)
