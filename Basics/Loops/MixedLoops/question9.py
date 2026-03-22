# Write a PATTERN GENERATOR using a while loop for rows and a for loop for printing stars in
# each row:

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
#         print("*", end=" ")

#     print()
#     row += 1

####another approach

# row = 1

# while row <= 5:
#     if row == 1 or row == 5:
#         stars = 1
#     elif row == 2 or row == 4:
#         stars = 3
#     else:  
#         stars = 5
    
#     for j in range(stars):
#         print("*", end="")
    
#     print() 
    
#     row += 1

####again optimal approach
star_counts = [1, 3, 5, 3, 1]

i = 0
while i < len(star_counts):
    count = star_counts[i]
    
    for j in range(count):
        print("*", end="")
    
    print()          
    i += 1
