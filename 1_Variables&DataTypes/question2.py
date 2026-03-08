# Ask the user to enter two numbers using input(). Add them, subtract them, multiply them, and
# divide them. Print each result. What goes wrong if you forget to convert the input? Show the
# broken version and the fixed version side by side in comments.

# ---------------- BROKEN VERSION ----------------
# Problem: input() returns STRING, not numbers.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Addition:", num1 + num2)        # String concatenation, not math
print("Subtraction:", num1 - num2)     # ERROR
print("Multiplication:", num1 * num2)  # ERROR
print("Division:", num1 / num2)        # ERROR


# Example if user enters:
# num1 = "5"
# num2 = "3"
# Addition result will be: "53" (strings joined)
# Subtraction / multiplication / division will raise TypeError


# ---------------- FIXED VERSION ----------------
# Solution: Convert input to numbers using int() or float()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)