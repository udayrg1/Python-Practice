'''
2. Your basic challenge 🧠
Scenario: QA Test Execution Initialization
You're preparing a new test execution cycle. Before testing begins, every test case must have the status "Not Executed".

Given:
test_cases = [    "TC101",    "TC102",    "TC103",    "TC104",    "TC105",    "TC106"]

Requirements
1. Create a dictionary using fromkeys().
2. Assign "Not Executed" to every test case.
3. Print the resulting dictionary.
4. Print the total number of test cases using len().

Expected output:
{    'TC101': 'Not Executed',    'TC102': 'Not Executed',    'TC103': 'Not Executed',    'TC104': 'Not Executed',    'TC105': 'Not Executed',    'TC106': 'Not Executed'}
6
'''

test_cases = [    "TC101",    "TC102",    "TC103",    "TC104",    "TC105",    "TC106"]

test_progress = dict.fromkeys(test_cases, "Not Executed")

print(test_progress)

print(len(test_progress))
