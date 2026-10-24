'''
Example: Employee salary records
Suppose you have a list of employee IDs:
'''
#regular approach

employee_ids = ["EMP101", "EMP102", "EMP103", "EMP104"]

employee_salary_data = {}

for emp_id in employee_ids:
    employee_salary_data[emp_id] = 0
print("Regular Approach: ", employee_salary_data)

#dict_comprehension
employee_ids = ["EMP101", "EMP102", "EMP103", "EMP104"]


employee_salaries = {emp_ids: 0 for emp_ids in employee_ids}

print("Dict Comprehension: ", employee_salaries)