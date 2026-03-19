# Use a while loop to compute the FACTORIAL of 6 (6! = 720). Print the result.

num = 6
factorial = 1

while num > 0:      
    factorial *= num
    num -= 1

print(factorial)