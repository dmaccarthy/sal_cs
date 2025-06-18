"""
This is a duplicate of a file needed for the example program p04_ex1.py.
Do not edit, move, or delete this file!

"""

def smallestFactor(n: int) -> int:
    "Calculate the smallest factor of a natural number"
    f = 2
    while f * f <= n:
        if n % f == 0: return f
        f += 1
    return n

def isPrime(n: int) -> bool:
    "Check whether a number is prime"
    return n > 1 and smallestFactor(n) == n
