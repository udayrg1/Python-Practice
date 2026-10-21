'''
Challenge 5 — Truthy and Falsy Values 🧠
A monitoring system stores failed test cases in a list.

failed_tests = []

Your task: Write an if-else statement that:
- Prints "Failed tests found" if the list contains one or more items.
- Prints "No failed tests" if the list is empty.

Constraint: Don't compare the list with [] or use len(). Let Python evaluate the list directly as a Boolean condition.
'''

failed_tests = []

if failed_tests:
    print("Failed tests found")
else:
    print("No failed tests")