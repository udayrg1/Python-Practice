'''
Pattern 3 of 6: Merge two lists without duplicates
Given:

list1 = [1, 3, 5, 7]

list2 = [3, 4, 5, 6, 8]

Expected result:

[1, 3, 5, 7, 4, 6, 8]
Your hints
1. Start with an empty result list.
2. Visit every element in the first list and add it.
3. Then visit every element in the second list.
4. Add a number only if it doesn't already exist in the result list.
Constraint: Don't use set(), and preserve the order of first appearance.
'''

list1 = [1, 3, 5, 7]

list2 = [3, 4, 5, 6, 8]

merged_list = []

for i in range(len(list1)):
    if list1[i] not in merged_list:
        merged_list.append(list1[i])

for j in range(len(list2)):
    if list2[j] not in merged_list:
        merged_list.append(list2[j])

print(merged_list)