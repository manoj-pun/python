# Using a for loop, print a right-angled triangle pattern of stars where each row has one more star
# than the previous. For n=5 the output should be: row 1 has 1 star, row 2 has 2 stars... row 5 has
# 5 stars. Then print the same triangle using a while loop. Then do it with a single list
# comprehension.


#for loop
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


#while loop
# n = 5
# i = 1

# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1

#comprehension
# n = 5
# [print("* " * i) for i in range(1, n + 1)]

#more pythonic
n = 5

for i in range(1, n + 1):
    print("* " * i)
