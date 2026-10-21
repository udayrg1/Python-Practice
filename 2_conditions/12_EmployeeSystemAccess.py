'''
Challenge 3 — Nested Conditions
Scenario: Employee System Access
An employee can access a restricted system only if they are an active employee. If they are active, check whether they have completed security training.
Given:
employee_active = Truesecurity_training_completed = False



Your task:
1. If the employee is active, check their security training status.
2. If training is completed, print "System Access Granted".
3. Otherwise, print "Complete Security Training First".
4. If the employee is not active, print "Access Denied: Inactive Employee".
'''

employee_active = True
security_training_completed = False

if employee_active:
    if security_training_completed:
        print("System Access Granted")
    else:
        print("Complete Security Training First")
else:
    print("Access Denied: Inactive Employee")