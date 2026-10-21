"""
Question 5: Convert CSV into List
Problem

Given:

Apple,Mango,Orange,Grapes

Convert it into a list.
"""

fruits = "Apple,Mango,Orange,Grapes"

fruits_list = fruits.split(",")

print(fruits_list)

"""
split(",") - is a method

splits the string wherever ',' appears.
"""