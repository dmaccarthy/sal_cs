"""
CSE 1120: Structured Programming
Flags & Counters
Example 3: Fibonacci Sequence

"""

currentNum = 0
nextNum = 1
remaining = 10
while remaining:
    print(currentNum)
    currentNum, nextNum = nextNum, currentNum + nextNum
    remaining -= 1
