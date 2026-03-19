# Use a for loop INSIDE a while loop: For each 'round' (rounds 1 to 3), print all numbers from 1 to 4.
# Label each round clearly.

round_num = 1

while round_num <= 3:
    print(f"Round {round_num}:")
    
    for num in range(1, 5):
        print(num)
    
    print() 
    round_num += 1