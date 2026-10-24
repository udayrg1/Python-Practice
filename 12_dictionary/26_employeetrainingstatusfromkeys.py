#Example 1: Initialize employee training status

employee_ids = ["EMP101", "EMP102", "EMP103", "EMP104"]

training_status = dict.fromkeys(employee_ids, "Not Started")

print(training_status)

#instead of writing five key-value pairs manually, you can use fromkeys()