# Write a while loop that asks the user to enter a number. Keep asking until the number is between 1
# and 10 (inclusive). When valid, print 'Valid input!'.
# Use: num = int(input('Enter a number: '))

num = int(input('Enter a number: '))

while num < 1 or num > 10:   
    num = int(input('Enter a number: '))  

print("Valid input!")