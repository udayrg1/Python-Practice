employee = {

    "name" : "Uday",
    "age" : 29,
    "department" : "Automation",
    "city" : "Hyderabad"
}

print("salary" in employee)   #Flase
del employee["city"]        
print(employee)               #{'name': 'Uday', 'age': 29, 'department': 'Automation'}    