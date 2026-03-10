# Given the string s = 'python programming is fun and python is powerful', write code that: counts
# how many times 'python' appears, replaces all occurrences with 'coding', checks if the result
# starts with 'coding', and prints the string in title case and in upper case.

s = "python programming is fun and python is powerful"

# 1. Count how many times 'python' appears
count_python = s.count("python")
print("Number of times 'python' appears:", count_python)

# 2. Replace all occurrences of 'python' with 'coding'
new_string = s.replace("python", "coding")
print("After replacement:", new_string)

# 3. Check if the result starts with 'coding'
starts_with_coding = new_string.startswith("coding")
print("Does the string start with 'coding'? ->", starts_with_coding)

# 4. Print the string in title case
print("Title Case:", new_string.title())

# 5. Print the string in upper case
print("Upper Case:", new_string.upper())

