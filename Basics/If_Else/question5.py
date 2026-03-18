# Use Python's one-line ternary expression to solve each of the
# following: (a) Find the absolute value of x = -9 without using abs() (b)
# Return 'Even' or 'Odd' for n = 17 (c) Clamp value = 150 to the range [0,
# 100] — if above 100 return 100, if below 0 return 0, else return value
# as-is

absvalue = -9
absolute = absvalue if absvalue >= 0 else -absvalue
print(absolute)

n = 17
EvenOdd = "Even" if n % 2 == 0 else "Odd"
print(EvenOdd)

value = 150
clampValue = 100 if value > 100 else 0 if value < 0 else value
print(clampValue) 