# Write a while loop to find the FIRST number greater than 1000 that is divisible by both 7 and 13.

num = 1001

while True:
    if num % 7 == 0 and num % 13 == 0:
        print(num)
        break
    num += 1