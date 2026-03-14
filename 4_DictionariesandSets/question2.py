# Write a function word_count(text) that takes a paragraph of text and returns a dictionary where
# each key is a word (lowercased) and each value is how many times it appears. Ignore
# punctuation. Then print the 5 most common words.

def word_count(text):
    counts = {}

    words = text.split()

    for word in words:
        word = word.strip('.,!?;:').lower()
        counts[word] = counts.get(word, 0) + 1

    return counts


text = "This is Manoj.Manoj is learning python and becoming better at python"

counts = word_count(text)

sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words[:5]:
    print(word, count)