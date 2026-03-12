# Given the list fruits = ['apple', 'banana', 'cherry', 'apple', 'mango', 'banana', 'apple'], write code to:
# count how many times each fruit appears, find the most common fruit, remove all duplicates
# while keeping order, and print the list sorted alphabetically.


fruits = ['apple', 'banana', 'cherry', 'apple', 'mango', 'banana', 'apple']

# 1️⃣ Count how many times each fruit appears
fruit_count = {}
for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

print("Count of each fruit:", fruit_count)

# 2️⃣ Find the most common fruit
most_common_fruit = max(fruit_count, key=fruit_count.get) #max(dictionary, key=dictionary.get) finds the key with the largest value
print("Most common fruit:", most_common_fruit)

# 3️⃣ Remove duplicates while keeping order
unique_fruits = []
seen = set()
for fruit in fruits:
    if fruit not in seen:
        unique_fruits.append(fruit)
        seen.add(fruit)

print("Unique fruits (original order):", unique_fruits)

# 4️⃣ List sorted alphabetically
sorted_fruits = sorted(unique_fruits)
print("Unique fruits (sorted alphabetically):", sorted_fruits)



