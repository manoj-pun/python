# Write a for loop using LIST COMPREHENSION to get squares of all odd numbers from 1 to 19.
# Then rewrite the same logic using a regular for loop with append(). Both should produce identical
# results.

# odd_numbers = [x**2 for x in range(1,20) if x % 2 != 0]
# print(odd_numbers)


#Using for loop
odd_numbers = []
for i in range(1,20):
    if i % 2 != 0:
        odd_numbers.append(i**2)
print(odd_numbers)
    