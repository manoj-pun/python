# Write a for loop that iterates over a dictionary and prints each KEY and VALUE pair neatly.
# student = {"name":"Alice", "age":20, "grade":"A", "city":"Kathmandu"}

student = {"name":"Alice", "age":20, "grade":"A", "city":"Kathmandu"}

for key,value in student.items():
    print(f"{key}: {value}")