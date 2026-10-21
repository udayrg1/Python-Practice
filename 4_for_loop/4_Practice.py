"""
🎯 Mini Challenge (Question 4)

Given:

employees = ["Ravi", "Uday", "Rahul", "Priya"]

Using enumerate() with start=1, print:

Employee 1: Ravi
Employee 2: Uday
Employee 3: Rahul
Employee 4: Priya

This will teach you the professional way of using enumerate(), and you'll use this exact pattern later when logging progress in your scraping scripts.
"""

employees = ["Madhur", "Venu", "Vamsi", "Uday"]

for index, employee in enumerate(employees, start=1):
    print(f"Employee {index}: {employee}")
