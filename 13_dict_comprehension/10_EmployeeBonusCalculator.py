'''
🚀 Next: Your final dictionary comprehension challenge
Let's test your understanding with a slightly more interview-oriented problem.

Challenge: Employee Bonus Calculator
employee_salaries = {    "EMP101": 60000,    "EMP102": 35000,    "EMP103": 80000,    "EMP104": 45000,    "EMP105": 25000,    "EMP106": 95000}


Requirements:
1. Create a dictionary named employee_bonuses using dictionary comprehension.
2. Employees earning ₹50,000 or more receive a 15% bonus.
3. Employees earning less than ₹50,000 receive a 5% bonus.
4. Store the bonus amount only, not the salary plus bonus.
5. Round each bonus to two decimal places.
6. Print the dictionary.

Expected output
{    'EMP101': 9000.0,    'EMP102': 1750.0,    'EMP103': 12000.0,    'EMP104': 2250.0,    'EMP105': 1250.0,    'EMP106': 14250.0}

Hint: Use if-else to choose between two bonus calculations. No filtering is required because every employee should be included.
'''

employee_salaries = {
    "EMP101": 60000,
    "EMP102": 35000,
    "EMP103": 80000,
    "EMP104": 45000,
    "EMP105": 25000,
    "EMP106": 95000
}

employee_bonuses = {employee : round((salary * 0.15), 2) if salary >= 50000 
                    else round ((salary * 0.05),2) for employee, salary in employee_salaries.items()}

print(employee_bonuses)

print(employee_salaries)