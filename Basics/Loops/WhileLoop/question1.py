# Write a while loop that starts at 1 and keeps DOUBLING the number until it exceeds 500. Print
# each value including the one that first exceeds 500.

num = 1

while True:          
    print(num)
    num *= 2
    if num > 500:   
        print(num)  
        break