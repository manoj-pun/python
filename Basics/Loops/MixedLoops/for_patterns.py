#Square with numbers
# 12345
# 12345
# 12345
# 12345

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()

############################################
#Column pattern
# 1111
# 2222
# 3333
# 4444

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()


############################################
# Alphabet triangle
# A
# AB
# ABC
# ABCD

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(chr(64 + j), end="")
#     print()

###########################################
# Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# number = 1

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(number, end=" ")
#         number += 1
#     print()

############################################
#Pascal’s Triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1

# Pascal's Triangle using while + for
# rows = 4
# i = 0  # row counter

# while i < rows:
#     # print spaces to center
#     for j in range(rows - i - 1):
#         print("", end="")

#     val = 1
#     for j in range(i + 1):
#         print(val, end=" ")
#         # update next value in row using combinatorial formula
#         val = val * (i - j) // (j + 1)

#     print()
#     i += 1

############################################
# Butterfly Pattern
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *

# Butterfly pattern using while + for
# rows = 4
# i = 1

# # Upper half
# while i <= rows:
#     # left stars
#     for j in range(i):
#         print("*", end="")
#     # spaces
#     for j in range(2 * (rows - i)):
#         print(" ", end="")
#     # right stars
#     for j in range(i):
#         print("*", end="")
#     print()
#     i += 1

# # Lower half
# i = rows
# while i >= 1:
#     # left stars
#     for j in range(i):
#         print("*", end="")
#     # spaces
#     for j in range(2 * (rows - i)):
#         print(" ", end="")
#     # right stars
#     for j in range(i):
#         print("*", end="")
#     print()
#     i -= 1

############################################

############################################

############################################
