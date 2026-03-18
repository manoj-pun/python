# Write an if-elif-else block that reads a student's score and prints their
# grade: 90–100 → 'A', 80–89 → 'B', 70–79 → 'C', 60–69 → 'D', below 60
# → 'F' Test with scores: 95, 82, 71, 65, 45

score = int(input("Enter a score: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

