"""
CSE 1120: Structured Programming
Flags & Counters
Example 2: Fibonacci Sequence

"""

currentNum = 0
nextNum = 1
count = 0
while count < 10:
    print(currentNum)
    currentNum, nextNum = nextNum, currentNum + nextNum
    count += 1
