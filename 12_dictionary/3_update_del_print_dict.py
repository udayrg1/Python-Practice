'''
Day 7 — Python Dictionary Practice 🐍
Prepare a Python dictionary named employee using these key-value pairs:
Key	Value
name	"Uday"
age	29
department	"Automation"

Requirements
1. Create the employee dictionary using the given key-value pairs.
2. Update age from 29 to 30.
3. Insert a new key salary with the value 60000.
4. Delete the department key and its associated value.
5. Print the total number of key-value pairs in the dictionary.
6. Check whether "department" exists in the dictionary and print the result.
7. Print the employee's current age using its key.
Your task: Write the complete program from scratch, including all seven requirements. Don't skip any print statements!
'''



employee = {

    "name" : "Uday",
    "age" : 29,
    "department" : "Automation"
}

employee["age"] = 30
employee["salary"] = 60000
del employee["department"]

print(len(employee))
print("department" in employee)
print(employee["age"])
print(employee)

