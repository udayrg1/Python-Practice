'''
Day 7 — Challenge: HR Performance Review
Employee Performance Analysis

An HR team stores employee performance scores in a dictionary named performance_scores.
Employee ID	Score
"EMP101"	78
"EMP102"	92
"EMP103"	65
"EMP104"	92
"EMP105"	48
"EMP106"	85
"EMP107"	65

Your requirements
1. Create the dictionary using the data above.
2. Create a new dictionary containing employees whose scores are 80 or above.
3. Count how many employees scored below 70.
4. Find the highest score and print the employee ID associated with it.
5. Find all employees who achieved that highest score and print their IDs as a list.

Expected output
{'EMP102': 92, 'EMP104': 92, 'EMP106': 85}
3
EMP102
['EMP102', 'EMP104']

Rules
- Write the complete program from scratch.
- Use loops and conditions for the filtering and counting.
- Don't hardcode the highest score or the employee IDs in your solution.
- Notice that two employees share the highest score. Your program must handle that correctly.
This challenge combines dictionary filtering, counting, maximum tracking, and handling duplicate maximum values.

'''
#1
performance_scores = {
    "EMP101":	78,
    "EMP102":	92,
    "EMP103":	65,
    "EMP104":	92,
    "EMP105":	48,
    "EMP106":	85,
    "EMP107":	65
}

#2
employee_with_high_scores = {}

for key, value in performance_scores.items():
    if value >= 80:
        employee_with_high_scores[key] = value
print(employee_with_high_scores)

#3
count = 0

for value in performance_scores.values():
    if value < 70:
        count += 1

print(count)

#4
highest_score_key = next(iter(performance_scores))
highest_score_value = performance_scores[highest_score_key]

for key, value in performance_scores.items():
    if value > highest_score_value:
        highest_score_key, highest_score_value = (key, value)

print(highest_score_key)

#5

highest_score_employees = []

for key, value in performance_scores.items():
    if value == highest_score_value:
        highest_score_employees.append(key)

print(highest_score_employees)