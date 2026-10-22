'''
Day 7 — Final challenge: Software Test Execution Report
QA Test Results Analysis

Imagine you're working as a Software Test Engineer. You've executed test cases for a new application release.

Create a dictionary named test_results with these key-value pairs:
Test case	Result
TC101	"Pass"
TC102	"Fail"
TC103	"Pass"
TC104	"Blocked"
TC105	"Fail"
TC106	"Pass"
TC107	"Blocked"
TC108	"Pass"

Requirements
1. Create a new dictionary containing only the failed test cases.
2. Count how many test cases passed.
3. Count how many test cases are blocked.
4. Calculate the pass percentage out of all test cases.
5. Print the test case IDs whose result is "Fail" or "Blocked" as a list.

Expected output
{'TC102': 'Fail', 'TC105': 'Fail'}
4
2
50.0
['TC102', 'TC104', 'TC105', 'TC107']



Rules for your final challenge
- Write the complete program from scratch.
- Use loops and conditions to process the dictionary.
- Calculate the percentage programmatically; don't hardcode 50.0.
- Avoid repeating the same loop unnecessarily where you can combine the logic sensibly.

'''

test_results = {

    "TC101" :	"Pass",
    "TC102" :	"Fail",
    "TC103" :	"Pass",
    "TC104" :	"Blocked",
    "TC105" :	"Fail",
    "TC106" :	"Pass",
    "TC107" :   "Blocked",
    "TC108" :	"Pass"
}


#1

failed_test_cases = {}

for key, value in test_results.items():
    if value == "Fail":
        failed_test_cases[key] = value
print(failed_test_cases)

#2

pass_count = 0

for value in test_results.values():
    if value == "Pass":
        pass_count += 1

print(pass_count)

#3

blocked_count = 0

for value in test_results.values():
    if value == "Blocked":
        blocked_count += 1

print(blocked_count)


#4

pass_percentage =  ((pass_count/len(test_results)))*100

print(pass_percentage)

#5

not_passed_testcase_ids = []

for key, value in test_results.items():
    if value == "Fail" or value == "Blocked":
        not_passed_testcase_ids.append(key)

print(not_passed_testcase_ids)