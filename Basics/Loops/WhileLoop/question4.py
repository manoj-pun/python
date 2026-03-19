# Use a while loop to REVERSE a number digit by digit.
# num = 12345 => reversed = 54321

num = 12345
reversed_number = 0

while num > 0:
    last_digit = num % 10
    reversed_number = reversed_number*10 + last_digit
    num //= 10

print(reversed_number)

