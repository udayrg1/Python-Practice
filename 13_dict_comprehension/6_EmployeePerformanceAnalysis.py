'''
🐍 Day 9 — Challenge 4: Employee Performance Analysis

Scenario: You're building an employee performance reporting system. HR wants to identify high-performing employees and classify their performance.

Input data

performance_scores = {
    "EMP101": 85,
    "EMP102": 62,
    "EMP103": 91,
    "EMP104": 45,
    "EMP105": 70,
    "EMP106": 96,
    "EMP107": 58
}

Requirements
Create a dictionary named high_performers using dictionary comprehension.
1. Include only employees whose scores are greater than or equal to 70.
2. If an employee's score is 90 or above, assign the value "Excellent".
3. Otherwise, assign "Good".
4. Preserve the employee IDs as dictionary keys.
5. Print the resulting dictionary and its length.

Expected output
{
    'EMP101': 'Good',
    'EMP103': 'Excellent',
    'EMP105': 'Good',
    'EMP106': 'Excellent'
}
4
'''

performance_scores = {
    "EMP101": 85,
    "EMP102": 62,
    "EMP103": 91,
    "EMP104": 45,
    "EMP105": 70,
    "EMP106": 96,
    "EMP107": 58
}

high_performers = {employee : "Excellent" if score >= 90  else "Good" for employee, score in performance_scores.items() if score >= 70}

print(high_performers)
print(len(high_performers))