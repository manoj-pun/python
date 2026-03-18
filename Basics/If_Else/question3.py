# Write nested if-else blocks to categorise a number as: 'Positive Even',
# 'Positive Odd', 'Negative Even', 'Negative Odd', or 'Zero' Test with: 8,
# 7, -4, -3, 0

num = int(input("Enter the number: "))

if num == 0:
    print("Zero")
else:
    if num > 0:
        # Positive branch
        if num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    else:
        # Negative branch
        if num % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")
    
