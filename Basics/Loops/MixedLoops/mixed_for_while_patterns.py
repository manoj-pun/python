# *
# ***
# *****
# ***
# *

row = 0
total_rows = 5

while row < total_rows:
    if row <= total_rows // 2:
        stars = 2 * row + 1
    else:
        stars = 2 * (total_rows - row) - 1

    for i in range(stars):
        print("*", end="")

    print()
    row += 1