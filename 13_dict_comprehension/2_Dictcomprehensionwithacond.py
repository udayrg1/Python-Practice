'''
3. Dictionary comprehension with a condition
You can also filter values using an if condition.

Suppose you have employee performance scores:
performance_scores = {    "EMP101": 78,    "EMP102": 92,    "EMP103": 65,    "EMP104": 88,    "EMP105": 48}

You want a new dictionary containing only employees whose scores are at least 80.
'''

performance_scores = {
    "EMP101": 78,
    "EMP102": 92,
    "EMP103": 65,
    "EMP104": 88,
    "EMP105": 48
}

#regular approach
high_scores = {}

for employee_id, score in performance_scores.items():
    if score >= 80:
        high_scores[employee_id] = score

print("Regular Approach: ",high_scores)

#dict comprehension

high_performers = {emp_id : scores for emp_id, scores in performance_scores.items() if scores >= 80}

print("Dict Comprehension: ",high_performers)



