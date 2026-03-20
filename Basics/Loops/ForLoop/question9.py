# Use a for loop with zip() to pair up two lists and print each pair.
# names = ["Alice","Bob","Carol"]
# scores = [85, 92, 78]
# Expected: Alice scored 85

names = ["Alice","Bob","Carol"]
scores = [85, 92, 78]

for name,score in zip(names,scores):
    print(f"{name} scored {score}")