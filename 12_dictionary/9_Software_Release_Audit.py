'''
Day 7 — Next challenge: Software Release Audit
Release Quality Control

A software company records the number of defects found in each release candidate.

Create a dictionary named release_defects with these key-value pairs:
Release	Defects
"RC1"	12
"RC2"	0
"RC3"	7
"RC4"	0
"RC5"	15
"RC6"	3

Your requirements
1. Create a new dictionary containing only releases that have at least one defect.
2. Print the new dictionary.
3. Print how many releases have zero defects.
4. Print the release with the highest defect count.

Expected output
{'RC1': 12, 'RC3': 7, 'RC5': 15, 'RC6': 3}
2
RC5
'''

release_defects = {
    "RC1" :	12,
    "RC2" : 0,
    "RC3" :	7,
    "RC4" :	0,
    "RC5" :	15,
    "RC6" : 3
}

#1. Create a new dictionary containing only releases that have at least one defect.

new_release_defects = {}
for key, value in release_defects.items():
    if value > 0:
        new_release_defects[key] = value

#2. Print the new dictionary.

print(new_release_defects)

#3. Print how many releases have zero defects.
count = 0
for value in release_defects.values():
    if value == 0:
        count += 1
print(count)

#4. Print the release with the highest defect count.

highest_release_defect_key = next(iter(release_defects))
highest_release_defect_value = release_defects[highest_release_defect_key]

for key, value in release_defects.items():
    if value > highest_release_defect_value:
       (highest_release_defect_key, highest_release_defect_value) = (key, value)

print(highest_release_defect_key)