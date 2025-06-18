"""
CSE 1120: Structured Programming
Accumulation
Example 2

"""

# Input
plain = "This is a secret message!"

# Processing
cypher = ""
for letter in plain:
    cypher += chr(ord(letter) + 3)

# Output
print(cypher)
