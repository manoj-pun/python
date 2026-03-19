# Use a for loop to find the SUM of all even numbers between 1 and 100 (inclusive). Print the final
# sum.

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)


# Better (more Pythonic)
print(sum(i for i in range(1, 101) if i % 2 == 0))

# Even smarter (step by 2)
total = 0
for i in range(2, 101, 2):
    total += i

print(total)
