'''
Step 3: Basic example
Consider a software release tracker problem and use popitem():
release_status = {    "release_101": "Completed",    "release_102": "Testing",    "release_103": "Pending"}


Output:
('release_103', 'Pending')
{'release_101': 'Completed', 'release_102': 'Testing'}
'''

release_status = {
    "release_101": "Completed",
    "release_102": "Testing",
    "release_103": "Pending"
}

result = release_status.popitem()
print(result)

print(release_status)