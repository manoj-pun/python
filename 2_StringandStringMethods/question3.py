# Write a function is_palindrome(text) that returns True if the text reads the same forwards and
# backwards, ignoring spaces and upper/lower case. Test it with: 'racecar', 'Hello', 'A man a plan canal Panama', 
# 'Was it a car or a cat I saw'.

# def is_palindrome(sentence):
#     splittext = sentence.split()       # remove spaces by splitting
#     jointext = "".join(splittext)      # join without spaces
#     lowertext = jointext.lower()       # convert to lowercase
#     reversetext = lowertext[::-1]      # reverse the string
    
#     if lowertext == reversetext:
#         return True
#     else:
#         return False

# print(is_palindrome("Was it a car or a cat I saw"))



#Pythonic version
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

# print(is_palindrome("Was it a car or a cat I saw"))

#Test with All Given Inputs
tests = [
    "racecar",
    "Hello",
    "A man a plan canal Panama",
    "Was it a car or a cat I saw"
]

for t in tests:
    print(t, "->", is_palindrome(t))