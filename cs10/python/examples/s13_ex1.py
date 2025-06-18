"""
CSE 1120: Structured Programming
Flags & Counters
Example 1

"""

waiting = True
while waiting:
  num = int(input("Please enter a number between 1 and 100: "))
  if num < 1 or num > 100:
    print("That number is not valid!")
  else:
    waiting = False
print("Your number is", num)
