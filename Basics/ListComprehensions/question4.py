# You have two lists of equal length. Use zip() inside a comprehension
# to produce a list of strings formatted as 'Alice scored 95'. names =
# ['Alice','Bob','Carol','Dave','Eve'] scores = [95, 82, 78, 90, 88]

names = ['Alice','Bob','Carol','Dave','Eve'] 
scores = [95, 82, 78, 90, 88]

names_scores = [f"{name} scored {score}" for name, score in zip(names, scores)]

print(names_scores)