# Write a function called reverse_words(sentence) that takes a sentence and returns it with the
# words in reverse order. 'Hello World' becomes 'World Hello'. Then write another version that
# also reverses each individual word's letters: 'Hello World' becomes 'olleH dlroW'.

#VERSION1
# def reverse_words(sentence):
#     # Split the sentence into words
#     words = sentence.split()
#     # Reverse the list of words
#     reversed_words = words[::-1]
#     # Join them back into a string
#     return " ".join(reversed_words)

# # Example usage
# s = "Hello World"
# print(reverse_words(s))  # Output: "World Hello"

#VERSION2
def reverse_words_letters(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse letters in each word
    reversed_letters_words = [word[::-1] for word in words]
    # Reverse the order of the words
    reversed_order = reversed_letters_words[::-1]
    # Join them back into a string
    return " ".join(reversed_order)

# Example usage
s = "Hello World"
print(reverse_words_letters(s))  # Output: "dlroW olleH"


