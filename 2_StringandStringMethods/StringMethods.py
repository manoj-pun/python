
##########CASE CONVERSION METHODS###########
#upper()
# text = "hello world"
# result = text.upper() #changes each letter to upper
# print(result)

#lower()
# text = "HellO WorLD"
# result = text.lower() #changes each letter to lower
# print(result)

#title()
# text = "hello world"
# result = text.title() #capitalizes each word
# print(result)

#capitalize()
# text = "hello world"
# result = text.capitalize() #capitalizes first letter
# print(result)

#swapcase()
# text = "Hello World"
# result = text.swapcase() #swaps lower to upper and upper to lower
# print(result)




#########Searching Methods############

#find()
# text = "python programming"
# result = text.find("pro") #Returns index (or -1 if not found)
# print(result)

#index()
# text = "python programming"
# result = text.index("z") #Returns index (error if not found)
# print(result)

#count()
# text = "python programming"
# result = text.count("m") #Counts occurrences
# print(result)

# startswith()
# text = "python programming"
# result = text.startswith("py") #checks beginning and shows result in boolean value
# print(result)

#endswith()
# text = "python programming"
# result = text.endswith("on") #checks ending and shows result in boolean value
# print(result)



##########Replace and Modify############

#replace()
# text = "I like Java"
# result = text.replace("like","hate") #replaces substring
# print(result)

#strip()
# text = " I like Python "
# result = text.strip() #by default it removes spaces
# print(result)

# text = "I like Java"
# result = text.strip("Java")
# print(result)

# lstrip()
# text = " I like python "
# print(len(text))
# result = text.lstrip() #removes left spaces
# print(len(result))
# print(result)

#rstrip()
# text = " I like python "
# print(len(text))
# result = text.rstrip() #removes right spaces
# print(len(result))
# print(result)

#or
# text = " I like python "
# result = text.rstrip() #removes right spaces
# print(repr(result))

#or
# text = " I like python "
# result = text.lstrip()
# print(f"[{result}]")

# or
# text = " I like python "
# result = text.lstrip().rstrip()
# print(repr(result))



#############Split and Join##########
# text = "mango,apple,banana"
# result = text.split()  #splits into list
# print(result)

#Syntax
# string.split(separator, maxsplit)
#separator-The character used to split the string
#maxsplit-Maximum number of splits
#If you don't provide anything, Python splits using whitespace (spaces, tabs, newlines).

# text = "Python is very powerful"
# result = text.split()
# print(result)
# #Python splits wherever it finds spaces
# # Returns a list of words

#using maxsplit
# text = "one two three four five"
# result = text.split(" ", 2)
# print(result)
#Python splits only 2 times
#Remaining string stays together

#rsplit()
# text = "apple,banana,cherry,date"
# # Split only once starting from the right
# result = text.rsplit(",", 1)
# print(result)

#join()
# Syntax
# separator.join(iterable)
# separator-The string placed between elements
# iterable-List, tuple, or other iterable of strings

# words = ["Python", "is", "awesome"]
# result = "".join(words)
# print(result)

numbers = ["2026", "03", "11"]
print("-".join(numbers))
