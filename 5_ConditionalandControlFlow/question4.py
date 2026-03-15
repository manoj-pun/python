# Write a function categorise_triangle(a, b, c) that takes three side lengths and: first checks if a
# valid triangle exists (any two sides must sum to more than the third), then classifies it as
# Equilateral (all equal), Isosceles (two equal), or Scalene (all different). Also classify by angles:
# Right, Acute, or Obtuse.

def categorise_triangle(a, b, c):

    # Step 1: Check if triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        print("Not a valid triangle")
        return

    # Step 2: Classify by sides
    if a == b == c:
        side_type = "Equilateral"
    elif a == b or a == c or b == c:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"

    # Step 3: Classify by angles
    sides = sorted([a, b, c])
    x, y, z = sides   # z is the largest side

    if x*x + y*y == z*z:
        angle_type = "Right"
    elif x*x + y*y > z*z:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"

    print(side_type, angle_type, "triangle")


categorise_triangle(4,3,5)

