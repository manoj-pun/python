# Given a sentence, produce a list where each word is replaced by a
# tuple of (word, len(word), word.upper()) — but only for words longer
# than 3 characters. sentence = 'list comprehensions are really powerful
# tools'

sentence = 'list comprehensions are really powerful tool'

# Split the sentence into words
words = sentence.split()

# List comprehension
new_sentence = [(word, len(word), word.upper()) for word in words if len(word) > 3]

print(new_sentence)