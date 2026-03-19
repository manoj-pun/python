# Write a GUESSING GAME: while loop for the main game, for loop for giving 3 hints when guess is
# wrong.
# secret=42, simulate with guesses=[10,55,42]

secret = 42

while True:
    num = int(input("Enter your guess: "))
    
    if num == secret:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess! Here are 3 hints:")
        
        for hint in range(1, 4):
            if hint == 1:
                print("Hint 1: Number is even")
            elif hint == 2:
                print("Hint 2: Number is greater than 40")
            else:
                print("Hint 3: Number is less than 50")



