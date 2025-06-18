"""
CSE 1110: Structured Programming
Data Types (Classes)
Question 2

"""

# Input
taxRate = 0.05
price = 4.99

# Do NOT modify any of the code below!

# Processing
tax = round(taxRate * price, 2)
total = price + tax

# Output
print(f"The sales tax is ${tax} and the total is ${total}.")
