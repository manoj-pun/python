# Use a for loop with the else clause. Print numbers 2 to 20. If 13 is found, break and skip else. If not
# found, else prints 'No 13 found!'. Now try a range that excludes 13 and observe the difference.

# for i in range(2, 21):
#     if i == 13:
#         break
#     print(i)  

# else:
#     print("No 13 found!")

# Output when 13 is excluded
for i in range(2, 13): 
    if i == 13:
        break
    print(i)
else:
    print("No 13 found!") 