# Write a for loop that iterates through a string and counts how many VOWELS (a,e,i,o,u) are
# present.
# sentence = "The quick brown fox jumps over the lazy dog"

sentence = "The quick brown fox jumps over the lazy dog"

vowels = 0
for i in sentence:
    if i.lower() in "aeiou":
        vowels += 1

print(vowels)