"""
CSE 1120: Structured Programming
Formatted Output
Example 3

"""

standings = [
    ("Pandas", 18, 2),
    ("Gryphons", 16, 4),
    ("Bears", 15, 5),
    ("Tigers", 11, 9),
    ("Lions", 7, 13),
    ("Sharks", 6, 14),
    ("Dinos", 3, 17)
]

# Print column headings
template = "{:^10s} {:>5s} {:>5s}"
print(template.format("TEAM", "Won", "Lost"))

# Print the data
template = "{:^10s} {:5d} {:5d}"
for team, won, lost in standings:
    print(template.format(team, won, lost))
