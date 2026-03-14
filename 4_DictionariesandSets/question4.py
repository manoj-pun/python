# You have a list of student dictionaries: [{'name':'Ali','grade':85,'city':'Kathmandu'}, ...]. Write code
# to group the students by city into a new dictionary where each key is a city and each value is a
# list of student names in that city, sorted alphabetically.

students = [
    {'name':'Ali','grade':85,'city':'Kathmandu'},
    {'name':'Sara','grade':90,'city':'Pokhara'},
    {'name':'Ram','grade':78,'city':'Kathmandu'},
    {'name':'Maya','grade':88,'city':'Pokhara'},
    {'name':'John','grade':92,'city':'Lalitpur'}
]

grouped = {}

for student in students:
    city = student['city']
    name = student['name']

    grouped.setdefault(city, []).append(name)

# sort names in each city
for city in grouped:
    grouped[city] = sorted(grouped[city])

print(grouped)