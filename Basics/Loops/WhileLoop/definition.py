# A while loop repeats a block of code as long as a condition is True.
# It is generally used when the number of iterations is unknown or depends on a dynamic condition.

# Sometimes, you don’t know exactly how many times you’ll repeat something.
# For example:

password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")

# How many times will the user enter the password?
# ❌ You don’t know in advance.
# The loop keeps going until the condition becomes false (password == "secret").
# This is what “unknown number of iterations” means.