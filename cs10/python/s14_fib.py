"""
CSE 1120: Structured Programming
Iteration & Searching
Question 1: Fibonacci Sequence

"""

# Modify the program to use a 'for' loop instead of a 'while' loop

currentNum = 0
nextNum = 1
count = 0
while count < 10:
    print(currentNum)
    currentNum, nextNum = nextNum, currentNum + nextNum
    count += 1
