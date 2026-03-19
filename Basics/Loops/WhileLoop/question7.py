# Write a while loop to find all PRIME NUMBERS between 10 and 50. A prime is only divisible by 1
# and itself. Print each prime.


# num = 10

# while num <= 50:
#     is_prime = True
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             is_prime = False
#             break
#         divisor += 1
#     if is_prime:
#         print(num)
#     num += 1


################
count = 0  # counts how many primes printed in current row

for num in range(2, 501):  # check numbers from 2 to 500
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num:4}", end=" ")
        count += 1
        
        if count % 10 == 0:
            print()  # move to next line