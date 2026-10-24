'''
🚀 Next challenge: Nested Data with Dictionary Comprehension

Let's try a slightly different problem that tests your understanding of dictionary values and conditions.

employee_scores = {    "EMP101": [85, 90, 78],    "EMP102": [55, 60, 65],    "EMP103": [95, 92, 98],    "EMP104": [70, 75, 80]}


Requirements:
1. Create a dictionary named employee_averages.
2. Use dictionary comprehension to calculate each employee's average score.
3. Round each average to two decimal places.
4. Keep employee IDs as keys.
5. Print the resulting dictionary.

Expected output:
{    'EMP101': 84.33,    'EMP102': 60.0,    'EMP103': 95.0,    'EMP104': 75.0}

Hint: Use sum() to calculate the total and len() to count the scores.
'''

employee_scores = {
    "EMP101": [85, 90, 78],
    "EMP102": [55, 60, 65],
    "EMP103": [95, 92, 98],
    "EMP104": [70, 75, 80]
}

employee_averages = {employee : round(sum(scores)/len(scores), 2) for employee, scores in employee_scores.items()}

print(employee_averages)