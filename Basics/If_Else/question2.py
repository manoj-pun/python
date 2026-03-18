# A theme park ride has these rules: - Must be at least 12 years old AND
# at least 140 cm tall, OR - Must be at least 18 years old (height doesn't
# matter then) Write an if-else block that prints 'Allowed' or 'Not
# Allowed'. Test: (age=14, height=145), (age=10, height=150), (age=18,
# height=120)

age = int(input("Enter the age: "))
height = float(input("Enter the height in cm: "))

if age < 12 and height < 140:
    print("Not allowed")
elif 12 <= age < 18 and height < 140:
    print("Not allowed")
else:
    print("Allowed")
