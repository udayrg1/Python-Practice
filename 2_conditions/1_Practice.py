"""
Question 1: Your First if Statement
Interview Definition

An if statement is used to execute a block of code only when a specified condition evaluates to True.

Problem

Given:

price = 75000

If the price is greater than 50000, print:

Premium Product
Expected Output
Premium Product
Hint

The syntax is:

if condition:
    # code
"""

price = int(input("Enter a price: "))

if price > 50000:
    print("Premium product")
else:
    print("Normal product")
