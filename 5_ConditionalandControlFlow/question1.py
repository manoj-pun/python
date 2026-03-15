# Write a function grade(score) that takes a number 0-100 and returns a letter grade: A (90+), B
# (80-89), C (70-79), D (60-69), F (below 60). Also handle invalid input: negative numbers or
# numbers above 100 should return 'Invalid'. Test with: 95, 82, 71, 65, 40, -5, 110.

def grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(grade(95))
print(grade(82))
print(grade(71))
print(grade(65))
print(grade(40))
print(grade(-5))
print(grade(110))