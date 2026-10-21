'''
🎯 Function Practice #6 — Employee Salary Analyzer

Now we're changing the problem type completely.

Create:

calculate_salary(basic_salary, bonus)

The function should:

Calculate the gross salary:
basic_salary + bonus
Calculate tax as 10% of the gross salary.
Calculate net salary:
gross salary - tax
Return both gross salary and net salary.

Test with:

basic_salary = 50000
bonus = 5000

Expected:

Gross Salary: 55000
Net Salary: 49500.0
🧠 Your thinking
basic salary + bonus
        ↓
   gross salary
        ↓
     10% tax
        ↓
    net salary
        ↓
return gross, net

This is your first function where you'll need to calculate multiple intermediate values and return multiple results.
'''

def calculate_salary(basic_salary, bonus):
    gross_salary = basic_salary + bonus
    tax = gross_salary * 10 / 100
    net_salary = gross_salary - tax

    return gross_salary, net_salary

gross_salary, net_salary = calculate_salary(50000, 5000)

print("Gross Salary: ", gross_salary)
print("Net Salary: ", net_salary)