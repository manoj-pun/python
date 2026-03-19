# Write a for loop to print this PATTERN (use only one loop variable):
# *
# **
# ***
# ****
# *****


for i in range(1,6):
    print("*"*i)


#incase of two loops allowed
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()



