# Start with the string ' 42.75 '. Show step by step: strip the spaces, convert to float, convert to int
# (notice the value lost), convert back to string, then check if the final string is numeric using
# .isnumeric(). Print a clear message at each step explaining what happened.

# Starting string
value = " 42.75 "
print(f"Original value: '{value}' | Type: {type(value)}")

# Step 1: Remove spaces using strip()
step1 = value.strip()
print(f"After strip(): '{step1}' | Type: {type(step1)}")
print("Explanation: Leading and trailing spaces were removed.\n")

# Step 2: Convert to float
step2 = float(step1)
print(f"After converting to float: {step2} | Type: {type(step2)}")
print("Explanation: The string was converted into a floating-point number.\n")

# Step 3: Convert float to int
step3 = int(step2)
print(f"After converting to int: {step3} | Type: {type(step3)}")
print("Explanation: The decimal part (.75) was LOST because integers store only whole numbers.\n")

# Step 4: Convert back to string
step4 = str(step3)
print(f"After converting back to string: '{step4}' | Type: {type(step4)}")
print("Explanation: The integer was converted back into a string.\n")

# Step 5: Check if the string is numeric
check = step4.isnumeric()
print(f"Is the final string numeric? {check}")
print("Explanation: '42' contains only digits, so isnumeric() returns True.")