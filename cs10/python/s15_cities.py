"""
CSE 1120: Structured Programming
Formatted Output
Question 2

"""

cities = [
    ("Toronto", 6202225),
    ("Montreal", 4291732),
    ("Vancouver", 2642825),
    ("Ottawa", 1488307),
    ("Calgary", 1481806),
    ("Edmonton", 1418118),
    ("Quebec", 839311),
    ("Winnipeg", 834678),
    ("Hamilton", 785184),
    ("Kitchener", 575847),
    ("London", 543551),
    ("Halifax", 465703),
    ("St. Catharines", 433604)
]

print("METRO", "Population")
for city, pop in cities:
    print(city, pop)
