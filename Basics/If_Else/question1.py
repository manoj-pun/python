# Write an if-elif-else block that reads a student's score and prints their
# grade: 90–100 → 'A', 80–89 → 'B', 70–79 → 'C', 60–69 → 'D', below 60
# → 'F' Test with scores: 95, 82, 71, 65, 45

score = int(input("Enter a score: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")

