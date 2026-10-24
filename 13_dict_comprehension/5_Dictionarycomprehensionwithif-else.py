'''
🚀 Next topic: Dictionary comprehension with if-else
Let's take it one step further!

You have employee performance scores. Assign a "Pass" status to employees scoring 70 or above and "Fail" to everyone else.

Your challenge:

performance_scores = {
    "EMP101": 85,
    "EMP102": 62,
    "EMP103": 91,
    "EMP104": 45,
    "EMP105": 70
}

Requirements:
1. Create a dictionary named employee_results.
2. Use dictionary comprehension with if-else.
3. Assign "Pass" if the score is greater than or equal to 70; otherwise, assign "Fail".
4. Print the resulting dictionary.

Expected output:

{
    'EMP101': 'Pass',
    'EMP102': 'Fail',
    'EMP103': 'Pass',
    'EMP104': 'Fail',
    'EMP105': 'Pass'
}

syntax = {key: value if condition else another_value for item in iterable}
'''

performance_scores = {
    "EMP101": 85,
    "EMP102": 62,
    "EMP103": 91,
    "EMP104": 45,
    "EMP105": 70
}

employee_results = {employee : "Pass" if result >= 70 else "Fail" for employee, result in performance_scores.items()}

print(employee_results)