# Create five variables: your name (string), your age (integer), your height in metres (float),
# whether you like Python (boolean), and the number of hours you code per week (integer). Print
# each one on its own line using an f-string that also shows the variable's type with type().

name = "Manoj"          # string
age = 22                # integer
height = 1.75           # float (in metres)
likes_python = True     # boolean
hours_per_week = 20     # integer

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Likes Python: {likes_python}, Type: {type(likes_python)}")
print(f"Coding Hours per Week: {hours_per_week}, Type: {type(hours_per_week)}")