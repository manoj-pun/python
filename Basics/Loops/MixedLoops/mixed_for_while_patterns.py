# *
# ***
# *****
# ***
# *

# row = 0
# total_rows = 5

# while row < total_rows:
#     if row <= total_rows // 2:
#         stars = 2 * row + 1
#     else:
#         stars = 2 * (total_rows - row) - 1

#     for i in range(stars):
#         print("*", end="")

#     print()
#     row += 1

################################
# Full pyramid
#     *
#    ***
#   *****
#  *******

# Full Pyramid Pattern
# rows = 4

# row = 0
# while row < rows:
#     # Print leading spaces
#     for i in range(rows - row - 1):
#         print(" ", end="")
    
#     # Print stars
#     for i in range(2 * row + 1):
#         print("*", end="")
    
#     print()        
#     row += 1

################################
#Inverted pyramid
# *******
#  *****
#   ***
#    *

# rows = 4
# row = 0

# while row < rows:
#     # Print leading spaces
#     for i in range(row):
#         print(" ", end="")
    
#     # Print stars (decreasing)
#     for i in range(2 * (rows - row) - 1):
#         print("*", end="")
    
#     print()          
#     row += 1

################################
#Full diamond
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# n = 7  

# if n % 2 == 0:
#     n += 1

# mid = (n + 1) // 2

# # Top half
# for i in range(1, mid + 1):
#     stars = 2 * i - 1
#     spaces = (n - stars) // 2
#     print(" " * spaces + "*" * stars)

# # Bottom half
# for i in range(mid - 1, 0, -1):
#     stars = 2 * i - 1
#     spaces = (n - stars) // 2
#     print(" " * spaces + "*" * stars)

################################
# Hollow Square
# *****
# *   *
# *   *
# *   *
# *****

# Hollow square using while + for (mixed)
# rows = 5
# i = 0
# while i < rows:
#     for j in range(rows):
#         # print * at borders
#         if i == 0 or i == rows-1 or j == 0 or j == rows-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     i += 1

################################
# Hollow Triangle
# *
# **
# * *
# *  *
# *****

# Hollow triangle using while + for
# rows = 5
# i = 1
# while i <= rows:
#     for j in range(1, i+1):
#         # first column, last column, or last row
#         if j == 1 or j == i or i == rows:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     i += 1
################################
# Number Pyramid
#     1
#    121
#   12321
#  1234321
# 123454321

# Number pyramid using while + for
rows = 5
i = 1
while i <= rows:
    # print spaces
    for j in range(rows - i):
        print(" ", end="")
    # print increasing numbers
    for j in range(1, i+1):
        print(j, end="")
    # print decreasing numbers
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()
    i += 1

################################