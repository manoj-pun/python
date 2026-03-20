# Use a for loop over sentences and a while loop inside to count occurrences of the word "the"
# (case-insensitive).
# sentences = ["The cat sat on the mat","There is no the in this","The dog chased the ball"]

sentences = [
    "The cat sat on the mat",
    "There is no the in this",
    "The dog chased the ball"
]

for sentence in sentences:
    words = sentence.lower().split()   
    
    i = 0
    count = 0
    
    while i < len(words):
        if words[i] == "the":
            count += 1
        i += 1
    
    print(f'"{sentence}" -> {count}')